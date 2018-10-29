#!_author_='Allen Lee'
# -*- coding: utf-8 -*-
import xlrd
import re
import requests
import ssl

class CustomFunction():
    
    def Cus_Open_Excel(self, file_path, sheet_name):
        """
        Function: gf_open_excel()
        Author: Allen Lee
        Description: Open excel from local excel
        Parameters:
                   file_path: excel path
                   sheet_name: the active sheet
        Return: worksheet - The object of the work sheet
        Example:gf_open_excel("../../Resource/TestData/testdata.xlsx", "sheet1")
        History:
               Added by Allen at Oct 26th,2018
        """
        try:
            work_book = xlrd.open_workbook(file_path)
            activate_sheet = work_book.sheet_by_name(sheet_name)

            return activate_sheet
        except Exception, e:
            print str(e)


    def Cus_Get_Rows_By_Tc_Id(self, tc_id, activate_sheet):
        """
        Function: gf_get_rows_by_tc_id()
        Author: Allen Lee
        Description: get the rows by Test case ID, if not found, return the warning message and then exit the script
        Parameters:
                   tc_id: Test Case ID
                   activate_sheet：Activate Sheet
        Return: list - et the rows by Test case ID, rows_list=[1,2,3,4]
        Example:gf_get_rows_by_tc_id("TC001",worksheet)

        History:
               Added by Allen at Oct 26th,2018
        """
        # initiate the rows
        row_list = []
        # activate the sheet
        # activate_sheet = Cus_Open_Excel(file_path, sheet_name)
        # get the number of rows
        num_rows = activate_sheet.nrows

        # data in columns 1, Test name should be in this columns which including Test ID as _, eg, TC2000_PM_XXXX
        first_col_values = activate_sheet.col_values(0)
        # initiate the pattern
        p = re.compile(r'_')
        for i in range(1, num_rows):
            # get the test case Id in column 0
            tc_id_in_col = p.split(first_col_values[i])[0]
            # complile test case Id  with tc_id
            if tc_id_in_col == tc_id:
                row_list.append(i)
                continue
        if len(row_list) == 0:
            print "Can not find the row by TC ID, please enter the correct TC ID"
            exit()
        return row_list


    def Cus_Get_Data_By_Col_Name_Row_Index(self, activate_sheet, row_index, col_name):
        """
        Function: gf_get_data_by_col_name_row_index()
        Author: Allen Lee
        Description: Get the test data by column name, if not found, pop up error message and exit the script
        Parameters:
                   row_index: row index
                   col_name:column name
                   activate_sheet：Activate Sheet
        Return: string - the data in special cell
        Example:gf_get_data_by_col_name_row_index(worksheet,2,"request_data")
        History:
               Added by Allen at Oct 26th,2018
        """

        # activate_sheet = Cus_Open_Excel(file_path, sheet_name)

        # get the number of columns
        num_cols = activate_sheet.ncols

        # data in row 1, Column Name should be in this row
        first_row_values = activate_sheet.row_values(0)
        for i in range(1, num_cols):
            if first_row_values[i] == col_name:
                col_index = i
                return activate_sheet.cell(int(row_index), int(col_index)).value
            elif i == num_cols - 1:
                print "Can not find the column by column name, please enter the correct column name"
                exit()


    def Cus_Split_String(self, string, split):
        """
        Function: GF_SplitString()
        Author: Allen Lee
        Parameters:
                   string: string you want to split
                   split:split characters, like "_"
        Description: Split string by split
        Example:gf_split_string(a_s_c, "_")
        History:
               Added by Allen at Oct 26th,2018
        """
        p = re.compile(split)
        return p.split(string)


    def Cus_Requests(self, requests_type, url, data=None, json=None, **kwargs):
        """
         Function: gf_requests()
           Author: Allen Lee
           Description: get the HTTP request types
           Parameters:
                      requests_type: HTTP request types: get, post, put, delete, head and options
                      url: HTTP request url
                      data: (optional) Dictionary, bytes, or file-like object to send in the body of the :class:`Request`.
                     json: (optional) json to send in the body of the :class:`Request`.
                     \*\*kwargs: Optional arguments that ``request`` takes.
           Return: requests.Response

           Example:gf_requests('POST', url, data=json_data, headers=headers)
           History:
                  Added by Allen at Oct 26th,2018
           """
   
        if str(requests_type) == "GET":
            url_response = requests.get(url, **kwargs)
            return url_response
        elif str(requests_type) == "POST":
            url_response = requests.post(url, data=data, json=json, **kwargs)
            return url_response
        elif str(requests_type) == "PUT":
            url_response = requests.put(url, data=data, **kwargs)
            return url_response
        elif str(requests_type) == "DELETE":
            url_response = requests.delete(url, **kwargs)
            return url_response
        elif str(requests_type) == "HEAD":
            url_response = requests.head(url, **kwargs)
            return url_response
        elif str(requests_type) == "OPTIONS":
            url_response = requests.options(url, **kwargs)
            return url_response
        else:
            print("Get the invalid HTTP request types, please enter the valid request type.")
            exit()

