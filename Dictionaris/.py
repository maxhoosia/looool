one_prob ={
    "day":"2022-10-19",
    "city":"Moskow",
    "prob":{
        "morning":-7,
        "evening":-2,
        "afternoon":-3
    }
}
one_prob1 ={
    "day":"2022-10-20",
    "city":"Moskow",
    "prob":{
        "morning":20,
        "evening":16,
        "afternoon":30
    }
}
one_prob2 ={
    "day":"2022-10-20",
    "city":"Kazan",
    "prob":{
        "morning":20,
        "evening":16,
        "afternoon":30
    }
}


page_prob =[one_prob,one_prob1,one_prob2]
answer_data =[]
one_data = {
    "nado ": 0,
    "city ":"gorod",
    "max_temp":{
        "size": 20,
        "day":"2022-30-60"
    },
    "min_temp":{
        "size": 20,
        "day":"2022-30-60"    
    }
}


def create_out_info(nado, city,  size_max, date_max, size_min, date_min):
    
    return  {
                "nado ": nado,
                "city ": city,
                "max_temp":{
                    "size": size_max,
                    "day":date_max
                },
                "min_temp":{
                    "size": size_min,
                    "day": date_min    
            }
}

perem = one_data["max_temp"]["size"] 
perem1 = one_data["min_temp"]["size"]
for i in range (len(page_prob)):
    a = page_prob[i]['city']
    for j in range (len(answer_data)):
        if a == answer_data[j]["city"]:
            answer_data[j]["nado"] = answer_data[j]["nado"]+1
        else :
            answer_data.append(one_data.copy())
            answer_data[j]["city"] = page_prob[i]['city']
    



# for i in range(len(page_prob)):
#     morn = page_prob[i]['prob']['morning']
#     after = page_prob[i]['prob']['afternoon']
#     even = page_prob[i]["prob"]["evening"]
#     if morn > perem:
#         perem = morn
#         one_data["max_temp"]["day"]=page_prob[i]["day"] 
#     elif after > perem:
#         perem = after
#         one_data["max_temp"]["day"]=page_prob[i]["day"] 
#     elif even > perem :
#         perem = even
#         one_data["max_temp"]["day"]=page_prob[i]["day"]
#     else :
#         perem = perem
#     if morn < perem1:
#         perem1 = morn
#         one_data["min_temp"]["day"]=page_prob[i]["day"] 
#     elif after < perem1:
#         perem1 = after
#         one_data["min_temp"]["day"]=page_prob[i]["day"] 
#     elif even < perem1 :
#         perem1 = even
#         one_data["min_temp"]["day"]=page_prob[i]["day"] 
#     else :
#         perem1 = perem1
    

# one_data["max_temp"]["size"] = perem
# one_data["min_temp"]["size"] = perem1
answer_data.append(one_data)
print(answer_data)
