*** Settings ***
Force Tags        Allen
Library           RequestsLibrary
Library           HttpLibrary
Library           CustomLibrary
Library           SeleniumLibrary

*** Test Cases ***
API_Testing
    [Tags]    Allen
    ${activate_sheet}    Cus_Open_Excel    TestData/Test.xlsx    ModuleName6
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

Baidu_Search
    [Tags]    Baidu
    Set Selenium Implicit Wait    05 seconds
    Open Browser    https://www.baidu.com/    Chrome
    Input Text    xpath=//input[@id='kw']    Python
    Click Element    xpath=//input[@id='su']
    Element Text Should Be    xpath=//h3['@class=t c-gap-bottom-small']/a/em    Python   
    Close Browser