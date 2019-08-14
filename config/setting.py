

"""
ENVIRONMENT_GRPC_CONFIG：grpc服务域名
"""
ENVIRONMENT_GRPC_CONFIG = {
    "dohko": {
        "order": "dohko.order.service.hualala.com:31515",
        # "order": "etcd://172.16.3.204:8081/dohko/order-service",
        # "order": "localhost:6565",
        "order-mock": "172.16.32.141:6565",
        "pos": "dohko.pos.service.hualala.com:31530",
        "equity": "equity.core.service.hualala.com:31731",
        "dzfp": "dohko.service.tax.hualala.com:31517",
        # "sms": "dohko.message.sender.hualala.com:31722",
        # "sms":"https://etcd.dohko.xh.hualala.com:5443/api/v1/watch/namespaces/dohko/endpoints/message-channel-service",
        "sms":"etcd://dohko.xh.hualala.com:5443/dohko/message-channel-service",
        # 查询短信签名用的域名message-channel-service
        "smschannel":"dohko.message.channel.hualala.com:31781",
        "adapi":"dohko.advert.service.hualala.com:31826",
        "equity2":"dohko.equity.account2.hualala.com",
        "smsdata":"dohko.data.statistical.query.hualala.com:31799",
        "semsms":"dohko.service.short.message.hualala.com:31524",
        "bop":"dohko.grpc.businessOperation.hualala.com:31806",
        "pay": "dohko.grpc.hualala.com:31827",
        "advert": "dohko.advert.service.hualala.com:31826",
        "host":"http://dohko.shop.hualala.com"

    }
}