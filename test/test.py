'''
Author: zhouyuchong
Date: 2024-12-09 11:37:58
Description: 
LastEditors: zhouyuchong
LastEditTime: 2024-12-18 10:51:05
'''
s = "### 重点产品：5G快线\n\n#### 一、市场分析\n\n1. **24年5G快线全省订购情况**\n   - 截至2024年8月，全省累积销售超700套，已在20个地市销售破零，实现流程拉通，发展势头良好，预计今年出货量2000套。\n\n2. **24年5G快线总体思路**\n   - 发挥网络速率、工业级网关、管理平台及小程序等优势，聚焦重点场景，加强一线赋能，完善线上线下渠道，采取融项目与入网格的组合拳，做大产品规模。\n\n#### 目标场景\n\n#### 客户需求\n   - 5G快线产品即插即用、移动便捷，无需现场布线和设备维护，您只需开通一张5G物联网卡和5G网关即可为您提供高性价比的5G专网服务。\n\n#### 产品核心功能及服务\n   - 融合“一张开通了B1 300G及以上档位的大流量卡 + 一个自研5G网关 + 免费使用的OneCyber管理平台”，打造“5G快线”轻量化5G专网产品，具备即插即用、简洁交付、移动便捷等优势。\n\n#### 价格体系\n   - 5G快线主套餐包含流量及5G网关，支持订购一次续费包供客户续约。一次性预存费用，一次性出账，按月计收。套餐总价已包含所有费用，不再额外收取物联网卡费等用。\n\n#### 优势分析\n   - 5G快线默认开通A1业务加速-5G极速功能，网络优先级6，理论下行1G、上行100M\n\n#### 七、销售关键方法\n\n1. **5G极速快线**\n   - 实现公网访问，首推资费125元/月，流量不限量，套餐内容详见300G 2年档，对标友商5G移动快线产品资费160元/月起，含流量50G。\n\n2. **5G备线专线**\n   - 实现内网备份，首推资费170元/月/点，至少2个点位，流量不限量，套餐内容详见500G 2年档，对标友商5G商企专网资费220元/月，含流量50G。\n\n3. **5G无线组网**\n   - 实现内网组网，首推资费227元/月/点，至少2个点位，每多增加一个点位，按227元/月计费，套餐内容详见800G 2年档。\n\n#### 八、交付及运维保障\n\n1. **订购、交付指引**\n   - 本业务订购、交付指引从客户发起订购开始，明确了订购、终端供货、空中写卡、交付、售后等流程的责任人及具体工作，以便于各环节工作衔接。\n\n2. **订购流程**\n   - 本流程涉及客户经理开卡审核流程、在CMIOT系统上开户流程等。\n\n#### 典型案例\n\n1. **案例介绍：宁波瑞幸咖啡**\n   - 宁波瑞幸咖啡品牌运营团队在新店拓展过程中，门店监控摄像头、点单机及咖啡机等设备需联网接入管理系统，为确保门店按时开业，并降低综合运营成本，运营团队采购了20套5G快线，用于难以使用有线联网的门店。因产品即插即用、高速稳定、管理便捷的产品特点获得了客户的认可，客户计划将5G快线在更多门店推广，潜在需求约100套。\n   - 项目亮点：快速安装，省去有线勘测开通时间，减少门店开业不确定性。统一管理，降低品牌运营团队协调、运维成本，提升运营综合效益。灵活部署，在门店退租后，5G快线可灵活调配至其他门店，降低迁移成本。\n   - 客户需求：品牌运营团队需要为门店协调部署网络，使用有线网络受限于街道及商场内宽带条件、业务办理人员配合度等多方面因素影响，可能造成门店联网时间、管理成本不可控，客户需要无线联网替代方案。品牌运营团队需要对各门店网络的部署、安装、使用、维护进行统一管理。\n\n2. **案例介绍：大连市老虎滩景区**\n   - 大连市老虎滩景区在实际运营中存在工作人员用网及偏远设施联网等需求，采用5G快线可以景区中灵活部署，方便工作人员用网以及给偏远设施进行无线联网，省去安装有线网络成本，提升了景区的运营效率，也进一步优化了游客的游览体验。\n   - 项目亮点：便捷安装，无需勘测拉线，快速使用网络，不受地理环境因素影响。\n   - 高速网络可为景区内营业点设备及工作人员提供网络，满足景区日常运营需求。\n   - 客户需求：景区内偏远地方设施进行有线网络搭建难度较大，施工周期长、施工成本高。景区内营业点设备及工作人员有用网需求。\n\n#### 十、面向客户的产品建议\n   - 针对连锁门店、视频直播、临时办公、工业组网、中小企业网络备线等重要场景，5G快线可以快速安装，省去有线建设开通时间，减少企业网络使用等待时间，同时在办公区域搬迁后，5G快线可灵活调配至其他办公区域，降低迁移成本"

text = s.split("####")
for i in range(len(text)):
    print("---", i, text[i])