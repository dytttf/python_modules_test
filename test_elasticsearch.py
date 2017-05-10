#coding:utf8
import elasticsearch

# 创建连接
'''
class Elasticsearch
    __init__(self, hosts=None, transport_class=<class 'elasticsearch.transport.Transport'>, **kwargs)
        host:
            type: list
            value: 1--> host:port
                   2--> {'host': host, 'port': port}
'''
es = elasticsearch.Elasticsearch(["localhost:9200"])

# 全局选项
# ignore 忽视某些返回码 400 or [400, 404]
# timeout 参数在建立es连接的时候 request_timeout 用在其他api操作的时候
# filter_path 用来在搜索时过滤返回的数据 ['hits.hits._id']

# 获取数据库信息
info = es.info()

# 获取索引
indexs = [x.get('index') for x in es.cat.indices()]

# 创建索引 数据库
try:
    test_index_name = 'test_index'
    es.indices.create(test_index_name, ignore=400)
except elasticsearch.exceptions.RequestError as e:
    if e.status_code == 400:
        print("索引 %s 已存在" % test_index_name)
    else:
        raise e

# 测试基本的增删改查
if 1:
    data_list = [
        {
        "name": "zhangsan",
        "sex": "m",
        },
        {
        "name": "lisi",
        "sex": "m",
        },
        {
        "name": "王五",
        "sex": "f",
        }
        ]

    # 插入数据
    for i, data in enumerate(data_list):
        resp = es.index(index=test_index_name, doc_type='test_type', id=i, body=data)
        # 以 doc_type 和 id 唯一定位一个文档 重复插入则覆盖
        #print(resp)

    # 查询数据
    # 两种方式 
    #    1 根据doc_type 和 id 唯一确定一个文档 es.get
    #    2 使用DSL语法搜索 es.search

    doc = es.get(index=test_index_name, doc_type='test_type', id='1')
    #print(doc)
    search_query = {
        "query":{
            "match_all": {}
            },
        # 这里写_source 好像没用 会被默认参数给覆盖掉
        "_source":["name"]
    }
    result = es.search(index=test_index_name,
                    body=search_query,
                    _source_include=['name'],
                    #filter_path=['hits.hits._id'],
                    )

    # 删除
    # 两种删除方法
    #    1 根据doc_type 和 id 唯一确定一个文档 es.delete
    #    2 根据DSL查询语法来删除 es.delete_by_query

    resp = es.delete(index=test_index_name, doc_type='test_type', id='1')
    search_query.pop('_source', '')
    # 接口有问题... 貌似废弃了
    if 0:
        result = es.delete_by_query(index=test_index_name,
                    body=search_query,
                    doc_type='test_type'
                    )

# 测试 Elasticsearch API
# 其他api都需要通过此api才能操作
if 1:
    # https://elasticsearch-py.readthedocs.io/en/master/api.html#elasticsearch
    pass

# 测试 indices API
if 1:
    pass

# 测试 ingest API
if 1:
    pass

# 测试 Cluster API
if 1:
    pass

# 测试 Nodes API
if 1:
    pass

# 测试 Cat API
if 1:
    # https://elasticsearch-py.readthedocs.io/en/master/api.html#cat
    # 获取别名信息
    aliases = es.cat.aliases()
    # 分片分布情况和磁盘使用情况
    allocation = es.cat.allocation()
    # 文档数
    count = es.cat.count()
    # 聚合内存使用情况
    fielddata = es.cat.fielddata()
    # 集群健康状态
    health = es.cat.health()
    # cat api接口文档
    cat_apis = es.cat.help()
    # 索引信息
    indices = es.cat.indices()
    # master信息
    master = es.cat.master()
    # 节点属性
    nodeattrs = es.cat.nodeattrs()
    # 节点列表  
    nodes = es.cat.nodes()
    # 待办任务
    pending_tasks = es.cat.pending_tasks()
    # 插件信息
    plugins = es.cat.plugins()
    # 
    recovery = es.cat.recovery()
    # 仓库信息
    repositories = es.cat.repositories()
    #
    segments = es.cat.segments()
    # 
    shards = es.cat.shards()
    # 
    # es.cat.snapshots()
    # es.cat.tasks()
    # es.cat.templates()
    # 线程池信息
    thread_pool = es.cat.thread_pool()

# 测试 Snapshot API
if 1:
    pass

# 测试 Tasks API
if 1:
    pass

