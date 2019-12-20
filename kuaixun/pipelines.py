# -*- encoding: utf-8 -*-

import pymysql as pq


class KuaixunPipeline(object):
    def __init__(self):
        self.conn = pq.connect(host='127.0.0.1', user='root', passwd='root', db='test', charset='utf8')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        ct = item['ct'].strip()
        title = item['title'].strip()
        content = ''.join(item['content']).strip()
        sql = 'INSERT INTO test (ct, title, content) VALUES (%s, %s, %s)'
        self.cur.execute(sql, (ct, title, content))
        self.conn.commit()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
