from django.db.models import Sum, Count
from django.db.models import F
from datetime import datetime 

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from api.utils.dataparser import ExcelParser
from api.utils.helper import load_excel
from api.models import Address, Budget, Project
from api.v1.serializers import ProjectSerializer


class FileUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        file = request.data['file']
        ep = ExcelParser(file)
        files_dict = ep.get_fields_value_dict()
        if files_dict:
            load_excel(files_dict)
        else:
            return Response({'error': 'The excel file format is not supported. Please contact system admin for more info.'}, status=400)
        return Response({'message': 'The excel file was processed successfully.'}, status=204)


class ProjectListView(APIView):
    
    def get(self, request, format=None):
        project = Project.objects.all()
        if 'sector' in request.GET:
            project = project.filter(sector=request.GET['sector'])
        if 'project_status' in request.GET:
            project = project.filter(project_status= request.GET['project_status'])
        if 'donor' in request.GET:
            project = project.filter(donor=request.GET['donor'])
        if 'humanitarian' in request.GET:
            project = project.filter(humanitarian=request.GET['humanitarian'])
        if 'agremeent_date' in request.GET:
            try:
                agremeent_date = datetime.strptime(request.GET['agremeent_date'], '%m-%d-%Y')
                project = project.filter(agremeent_date=agremeent_date)
            except Exception as e:
                print(e)
                return Response({'error':'The format of input date is not supported.'}, status=400)
        if 'effective_date' in request.GET:
            try:
                effective_date = datetime.strptime(request.GET['effective_date'], '%m-%d-%Y')
            except Exception as e:
                print(e)
                return Response({'error':'The format of input date is  not supported.'}, status=400)
            project = project.filter(effective_date=effective_date)
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data, status=200)
        

class SummaryView(APIView):

    def get(self, request):
        project_info = Address.objects.all()
        if 'sector' in request.GET:
            project_info = project_info.filter(project__sector=request.GET['sector'])
        if 'project_status' in request.GET:
            project_info = project_info.filter(project__project_status= request.GET['project_status'])
        if 'donor' in request.GET:
            project_info = project_info.filter(project__donor=request.GET['donor'])
        if 'humanitarian' in request.GET:
            project_info = project_info.filter(project__humanitarian=request.GET['humanitarian'])
        if 'agremeent_date' in request.GET:
            try:
                agremeent_date = datetime.strptime(request.GET['agremeent_date'], '%m-%d-%Y')
                project_info = project_info.filter(project__agremeent_date=agremeent_date)
            except Exception as e:
                print(e)
                return Response({'error':'The format of input date is not supported.'}, status=400)
        if 'effective_date' in request.GET:
            try:
                effective_date = datetime.strptime(request.GET['effective_date'], '%m-%d-%Y')
                project_info = project_info.filter(project__effective_date=effective_date)
            except Exception as e:
                print(e)
                return Response({'error':'The format of input date is  not supported.'}, status=400)

        # total budget and project count 
        aggregate_result = project_info.aggregate(
            total_budget=Sum('budget__commitments'),
            project_count=Count('project'),
        )


        # for sector part 
        sector_objs = project_info.values('project__sector').annotate(
            sector_name = F('project__sector'),
            total_budget = Sum('budget__commitments'),
            project_counts = Count('project')
        ).values('total_budget', 'project_counts', 'sector_name')

        sector_list = list()
        for obj in sector_objs:
            obj_dict = {}
            obj_dict['name'] = obj['sector_name']
            obj_dict['total_budget'] = obj['total_budget']
            obj_dict['project_counts'] = obj['project_counts']
            sector_list.append(obj_dict)
        aggregate_result["sector"] = sector_list

        return Response(aggregate_result, status=200)


class CounterView(APIView):

    def get(self, request):
        project_obj = Address.objects.all()
        proj_obj = project_obj.values('municipality').annotate(
            budget = Sum('budget__commitments'),
            project_count = Count('project')
        )
        if 'province' in request.GET:
            proj_obj = project_obj.filter(province=request.GET['province']).values('province').annotate(
                budget = Sum('budget__commitments'),
                project_count = Count('project')
            )
        if 'district' in request.GET:
            proj_obj = project_obj.filter(district=request.GET['district']).values('district').annotate(
                budget = Sum('budget__commitments'),
                project_count = Count('project')
            )
        return Response(proj_obj, status=200)