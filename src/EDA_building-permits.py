import pandas as pd


df = pd.read_csv('/Users/vinicius/Building_permit/data/raw/issued-building-permits.csv', sep=';')

df.head()


# https://plposweb.vancouver.ca/Public/Default.aspx?PosseMenuName=PC_Search
# cruzar informação com esse site para verificar se o building permit tem plumbing permit, sendo o caso de não ter, maior possibilidade de ser um bom lead.



df.columns

df.PermitCategory.unique()
df.TypeOfWork.unique()

df.SpecificUseCategory.unique()


df.PropertyUse.unique()
df.PropertyUse.nunique()
'temos 154 opções de property use, olhando por cima diz oque sera a construção ex:. academia, escritório, hospital.....''

df.SpecificUseCategory.nunique()
# parece um pouco de overlap do propertyUse, mas tem 990 uniques nessa coluna indicando mais granularidade

# ----------------------
# visualização e frame das colunas
# [['PermitNumberCreatedDate', 'IssueDate',
#        'PermitElapsedDays', 'ProjectValue', 'TypeOfWork', 'Address',
#        'ProjectDescription', 'PermitCategory', 'Applicant', 'ApplicantAddress', 'SpecificUseCategory', 'BuildingContractor',
#        'BuildingContractorAddress',
#        'YearMonth']]

      
ds_time_and_money = df[['PermitNumberCreatedDate', 'IssueDate',
       'PermitElapsedDays', 'ProjectValue', 
       'YearMonth']]
       
ds_time_and_money.head(4)

ds_time_and_money.shape

# qual o tamanho dos projetos que temos condição de pegar? até 150.000?

ds_time_and_money[ds_time_and_money['ProjectValue'] <= 150000]

# quais tipos são os melhores para trabalhar e com maior margem ? restaurante, office, renovation de casa....

# quais tipos não pegaria (filter out) highrises....