# crud: 增删改查。create/retrieve/update/delete
from dbconn import Session, Departments, Employees

# 建立到数据库的会话连接
session = Session()

# 创建部门
hr = Departments(dep_id=1, dep_name='人事部')
ops = Departments(dep_id=2, dep_name='运维部')
dev = Departments(dep_id=3, dep_name='开发部')
qa = Departments(dep_id=4, dep_name='测试部')
market = Departments(dep_id=5, dep_name='市场部')
sales = Departments(dep_id=6, dep_name='销售部')
# 通过会话操作数据库
# session.add_all([hr, ops, dev, qa, market, sales])

# 创建员工
lb = Employees(
    emp_id=1, emp_name='刘备', birth_date='1970-1-10',
    email='lb@tedu.cn', dep_id=1
)
gy = Employees(
    emp_id=2, emp_name='关羽', birth_date='1971-2-8',
    email='gy@tedu.cn', dep_id=2
)
zf = Employees(
    emp_id=3, emp_name='张飞', birth_date='1973-4-20',
    email='zf@qq.com', dep_id=2
)
zy = Employees(
    emp_id=4, emp_name='赵云', birth_date='1980-10-3',
    email='zy@163.com', dep_id=3
)
# session.add_all([lb, gy, zf, zy])
####################################
# 查询时，直接查询类，返回的是类的所有实例
qset1 = session.query(Departments)
print(qset1)  # qset1只是查询语句，取值时，才会真正连接数据库
# 从qset1中取值，方法一，使用all方法返回列表
# result1 = qset1.all()
# print(result1)
# 从qset1中取值，方法二，直接遍历
for dep in qset1:
    print(dep.dep_id, dep.dep_name)



# 确认
session.commit()

# 关闭会话
session.close()

