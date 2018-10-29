*** Settings ***
Library           CustomLibrary
Library           RequestsLibrary
Library           HttpLibrary
Library           HttpLibrary.HTTP

*** Test Cases ***
test123
    ${123}    Evaluate    inspect.stack()[13]    inspect
    ${InstanceID}    Get Library Instance    all=True
    ${json_data}    Set Variable    1    2
    @{list}    Create List    data=${json_data}    1=2    12=3
    ${count}    Get Length    ${list}
    ${list1}    Create List    23    43=34
    log many    @{list}
    log many    @{list}[0]
    log    @{list}[1]
    log    @{list}[2]
    log many    ${list1}

API_Testing
    ${activate_sheet}    Cus_Open_Excel    ../Project_Name/TestData/Test.xlsx    ModuleName6
    @{Data_Rows}    Cus_Get_Rows_By_Tc_Id    TC3456    ${activate_sheet}
    : FOR    ${i}    IN    @{Data_Rows}
    \    ${request_data}    Cus_Get_Data_By_Col_Name_Row_Index    ${activate_sheet}    ${i}    data
    \    ${request_tpye}    Cus_Get_Data_By_Col_Name_Row_Index    ${activate_sheet}    ${i}    request_tpye
    \    ${request_url}    Cus_Get_Data_By_Col_Name_Row_Index    ${activate_sheet}    ${i}    request_url
    \    ${request_headers}    Cus_Get_Data_By_Col_Name_Row_Index    ${activate_sheet}    ${i}    headers
    \    ${expect}    Cus_Get_Data_By_Col_Name_Row_Index    ${activate_sheet}    ${i}    expect
    \    ${json_data}    Evaluate    demjson.encode(${request_headers})    demjson
    \    ${json_headers}    Evaluate    demjson.encode(${request_headers})    demjson
    \    ${json_headers_1}    To Json    ${json_headers}
    \    ${false}    Convert To Boolean    False
    \    ${expect}    Convert To Integer    ${expect}
    \    ${resp}    Cus_Requests    ${request_tpye}    ${request_url}    data=${request_data}    headers=${json_headers_1}
    \    ...    verify=${false}
    \    Should Be Equal As Strings    ${resp.status_code}    ${expect}
