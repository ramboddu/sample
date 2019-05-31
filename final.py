
import json
from collections import OrderedDict

def stringParse(queryResult):
        columns=[]
        splitlist = queryResult.split("\n")
        flag=0
        position=0
        for line in splitlist:
            
            if flag==0:
                if not line.startswith("----"):
                    continue
                else:
                    flag=1
            else:
                if len(line)>0 and "rows selected" not in line:
                    temp = OrderedDict()
                    #temp={}
                    position+=1
                    
                    print("This is line #  %u"  % position)
                    splittab = line.split()
                    for tb_counter in range(0, len(splittab)):
                        if tb_counter==0:
                            name=splittab[tb_counter]
                        if tb_counter==1:
                            if splittab[tb_counter].lower()!="date" and splittab[tb_counter].lower()!="timestamp":
                                datatype="string"
                            else:
                                dt_temp = OrderedDict()
                                #dt_temp={}
                                if splittab[tb_counter].lower()=="date": 
                                    base="date"
                                    formatt="mm/dd/yyyy"
                                if splittab[tb_counter].lower()=="timestamp":    
                                    base="timestamp"
                                    formatt="yyyy-mm-dd hh:mm:ss"
                                dt_temp["base"]=base
                                dt_temp["format"]=formatt
                                datatype=dt_temp
                    temp["position"]=position
                    temp["name"]=name
                    temp["datatype"]=datatype
                    columns.append(temp)
        print(columns)
        return columns        

def toJson(queryResult):
    dialect= OrderedDict()
    #dialect={}
    dialect["delimiter"]=","
    dialect["doubleQuote"]=True
    dialect["encoding"]="utf-8"
    dialect["header"]=True
    
    columns=stringParse(queryResult)
    #tableSchema={}
    tableSchema= OrderedDict()
    tableSchema["columns"]=columns
    pre_json= OrderedDict()
    #pre_json={}
    pre_json["dialect"]=dialect
    pre_json["tableSchema"]=tableSchema
    #return pre_json
    # if want to write json data into file use this
    json_file="my_output_file"
    with open(json_file,"w") as fh:
                    json.dump(pre_json,fh,indent=4)
    
    ##if just want json output use this
    #final_json=json.dumps(pre_json,indent=4)
    #print("final_json",final_json)


#get queryResult here
queryResult="""

NAME      TYPE

-----------------------------

SMITH     Number
ALLEN     varchar
date      Date
timestamp timestamp
4 rows selected.
"""
#call toJson to write json file
toJson(queryResult)