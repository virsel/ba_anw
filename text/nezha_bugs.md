1.

```
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
```
- falls resource alert in kandidat aber nicht passend zu ziel rca
    - topk counter wird nicht inkrementiert