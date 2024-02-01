import requests
from openpyxl import Workbook
# pip install openpyxl
import xlrd

# GitLab API相关配置
GITLAB_URL = 'https://gitlab.devops.cmft/industrygroup'  # GitLab实例URL
PRIVATE_TOKEN = 'HYCWebhFVHwJqut5yTxq'  # 替换为您的GitLab私有访问令牌

# Excel表格相关配置
EXCEL_FILE = 'gitlab_permissions.xlsx'  # Excel文件名
SHEET_NAME = 'Permissions'  # 工作表名称



def get_projects():
    headers = {'Private-Token': PRIVATE_TOKEN}
    params = {'membership': 'true','per_page': 100}  # 调整每页项目数量
    url = f'{GITLAB_URL}/api/v4/projects'
    response = requests.get(url, headers=headers, params=params)
    projects = response.json()
    return projects

def get_project_members(project_id):
    headers = {'Private-Token': PRIVATE_TOKEN}
    url = f'{GITLAB_URL}/api/v4/projects/{project_id}/members/all'
    response = requests.get(url, headers=headers)
    members = response.json()
    return members

def create_excel(projects):
    wb = Workbook()
    sheet = wb.active
    sheet.title = SHEET_NAME
    sheet.append(['Project Name', 'Username', 'Role'])

    for project in projects:
        print(project)
        project_name = project['name_with_namespace']
        project_id = project['id']
        members = get_project_members(project_id)
        for member in members:
            username = member['username']
            access_level = member['access_level']
            sheet.append([project_name, username, access_level])

    wb.save(EXCEL_FILE)
    print(f'Excel file "{EXCEL_FILE}" created successfully.')

workbookyuan = xlrd.open_workbook('projectlist0605.xlsx')
tableProject = workbookyuan.sheet_by_name(sheet_name='Sheet1')

if __name__ == '__main__':
    projects = get_projects()
    print(projects)
    create_excel(projects)
