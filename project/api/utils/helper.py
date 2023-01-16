from api.models import Address, Budget, Project

def load_excel(excel_data):
    for province, district, municipality, project_title, project_status, donor, executing_agency,\
        implementing_partner, counterpart_agency, assistance_code, humanitarian, sector,\
            commitments, agremeent_date, effective_date, budget_type, sector_code in zip(excel_data["province"],
            excel_data["district"],excel_data["municipality"], excel_data["project_title"], 
            excel_data["project_status"], excel_data["donor"], excel_data["executing_agency"], 
            excel_data["implementing_partner"], excel_data["counterpart_agency"], excel_data["assistance_code"],
            excel_data["humanitarian"], excel_data["sector"], excel_data["commitments"], excel_data["agremeent_date"],
            excel_data["effective_date"], excel_data["budget_type"], excel_data["sector_code"]
            ):

        if project_status == 'On-Going':
            project_status = 'O'
        else:
            project_status = 'C'

        if budget_type == 'Off Budget':
            budget_type = 'OFF'
        else:
            budget_type = 'ON'

        if humanitarian == 'No':
            humanitarian = False
        else:
            humanitarian=True

        proj_obj = Project.objects.filter(
            project_title=project_title, 
            project_status=project_status,
            donor=donor, 
            executing_agency=executing_agency, 
            implementing_partner=implementing_partner,
            counterpart_agency=counterpart_agency, 
            humanitarian=humanitarian, 
            assistance_code=assistance_code,
            agremeent_date=agremeent_date,
            effective_date=effective_date
        )

        if not proj_obj.exists():
            proj_obj = Project.objects.create(
                project_title=project_title, 
                project_status=project_status,
                donor=donor, 
                executing_agency=executing_agency, 
                implementing_partner=implementing_partner,
                counterpart_agency=counterpart_agency, 
                humanitarian=humanitarian, 
                assistance_code=assistance_code,
                agremeent_date=agremeent_date,
                effective_date=effective_date,
                sector=sector, 
                sector_code=sector_code
            )
        else:
            proj_obj = proj_obj.first()

        budget_obj = Budget.objects.filter(
            commitments=commitments, 
            budget_type=budget_type, 
        )

        if not budget_obj.exists():
            budget_obj = Budget.objects.create(
                commitments=commitments, 
                budget_type=budget_type, 
            )
        else:
            budget_obj = budget_obj.first()

       
        addr_obj = Address.objects.filter(
            project=proj_obj,
            budget=budget_obj,
            province=province, 
            district=district, 
            municipality=municipality
        )
        if not  addr_obj.exists():
            addr_obj = Address.objects.create(
                project=proj_obj,
                budget=budget_obj,
                province=province, 
                district=district, 
                municipality=municipality
            )

        