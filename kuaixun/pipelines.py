import pymysql as pq
import json

class KuaixunPipeline(object):
	def __init__(self):
		self.file =  open('item.jl', 'wb')
		#数据库连接数据需要填写
		self.conn = pq.connect(host='xxx.xxx.xxx.xxx', user='xxxx', passwd='xxxx',
				db='xxxx', charset='utf8')
		self.cur = self.conn.cursor()

	def process_item(self, item, spider):
		#line = json.dumps(dict(item)) + "\n"
		#self.file.write(line)
		ct = item['ct']
		title = item['title']
		content = ''.join(item['content']).strip()
		sql = 'insert into test (ct, title, content) values (%s, %s, %s)'
		self.cur.execute(sql,(ct, title, content))
		res = self.conn.commit()

	def close_spider(self, spider):
		self.cur.close()
		self.conn.close()
