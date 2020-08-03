将kafka的数据sink到clickhouse：
配置注意点：
+ config.json中："minBufferSize": 3,
+ task的配置中需要去除MATERIALIZED的列： "excludeColumns" : ["time"],
+ 