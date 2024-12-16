# nezha bug:
topk = 1

inject_service = fault["inject_pod"].rsplit('-', 1)[0]
inject_service = inject_service.rsplit('-', 1)[0]

root_cause = root_cause_list[inject_service][fault["inject_type"]].split(
    "_")

if len(root_cause) == 1:
    for i in range(len(result_list)):
        if "resource" in result_list[i].keys():
            if str(root_cause[0]) in str(result_list[i]["resource"]) and str(fault["inject_pod"]) in str(result_list[i]["pod"]):
                top_list.append(topk)
                logger.info("%s Inject Ground Truth: %s, %s score %s", fault["inject_time"],
                            fault["inject_pod"], fault["inject_type"], topk)
                break
        else:
            if i > 0:
                if result_list[i-1]["score"] == result_list[i]["score"] and result_list[i-1]["deepth"] == result_list[i]["deepth"]:
                    continue
                else:
                    topk = topk + 1
            elif i == 0:
                topk = topk + 1
elif len(root_cause) == 2:
    for i in range(len(result_list)):
        if root_cause[0] in from_id_to_template(int(result_list[i]["events"].split(
                "_")[0]),log_template_miner) and root_cause[1] in from_id_to_template(int(result_list[i]["events"].split("_")[1]),log_template_miner) and str(fault["inject_pod"]) in str(result_list[i]["pod"]):
            top_list.append(topk)
            logger.info("%s Inject Ground Truth: %s, %s score %s", fault["inject_time"],
                        fault["inject_pod"], fault["inject_type"], topk)
            break
        else:
            if i > 0:
                # logger.info("%s, %s",
                #             result_list[i-1]["score"], result_list[i]["score"])
                if result_list[i-1]["score"] == result_list[i]["score"] and result_list[i-1]["deepth"] == result_list[i]["deepth"]:
                    continue
                else:
                    topk = topk + 1
            elif i == 0:
                topk = topk + 1
                
                
# correct:
def get_nezha_rank(result_list, root_cause, inject_pod):
    rank = 1
    rc_found_flag = False
            
    if len(root_cause) == 1:
        for i in range(len(result_list)):
            if "resource_alert" in result_list[i].keys():
                if str(root_cause[0]) in str(result_list[i]["resource_alert"]) and inject_pod in str(result_list[i]["pod"]):
                    rc_found_flag = True
                    break
            else:
                if "events_actual" in result_list[i].keys() and str(root_cause[0]) in from_id_to_template(int(result_list[i]["events_actual"].split("_")[1]),log_template_miner) and inject_pod in str(result_list[i]["pod"]):
                    rc_found_flag = True
                    break
                if i > 0:
                    if result_list[i-1]["score"] == result_list[i]["score"] and result_list[i-1]["deepth"] == result_list[i]["deepth"]:
                        continue
            rank += 1
            
    elif len(root_cause) == 2:
        for i in range(len(result_list)):
            if root_cause[0] in from_id_to_template(int(result_list[i]["events"].split(
                    "_")[0]),log_template_miner) and root_cause[1] in from_id_to_template(int(result_list[i]["events"].split("_")[1]),log_template_miner) and inject_pod in str(result_list[i]["pod"]):
                rc_found_flag = True
                break
            else:
                if i > 0:
                    # logger.info("%s, %s",
                    #             result_list[i-1]["score"], result_list[i]["score"])
                    if result_list[i-1]["score"] == result_list[i]["score"] and result_list[i-1]["deepth"] == result_list[i]["deepth"]:
                        continue
            rank += 1
    
    if not rc_found_flag:
        return -1
    return rank