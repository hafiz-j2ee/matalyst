import json
import web
import validation
import redis
import math
from matalyst.list.sorting import Ascending

class Get:
	def GET(self):
		self.render = web.template.render('templates')
		return self.render.factors()
	def POST(self):
		try:
			cache = redis.StrictRedis(host='redis', port=6379, db=0)
		except:
			cache = None
		outputDic={}
		outputString=None
		try:
			data=json.loads(web.data())
			isInteger=validation.IsInteger()
			outputDic=isInteger.checkNumber(data)
			if outputDic['status'] == 'OK':
				if cache is not None:
					outputString = cache.get(outputDic['number'])
				if outputString is not None:
					return outputString
				if outputDic['number']>0 or outputDic['number']<=999999999999:
					outputDic['factorsList']=Ascending().sortListAsc(self.findFactors(outputDic['number']))
				else:
					outputDic['status']='ERROR'
					outputDic['error']="Enter a positive intiger number."
		except Exception as e:
			print e
			outputDic['status']='ERROR'
			outputDic['error']="Data format is not validate"
		outputString = json.dumps(outputDic)
		if outputDic['status'] == 'OK' and cache is not None:
			cache.set(outputDic['number'], outputString)
		return outputString
	def findFactors(self, num):
		if num==1:
		    return [1]
		factors=[1,num]
		if num==2:
		    return factors
		incr=1
		if num%2==0:
		    factors.append(2)
		    factors.append(num/2)
		else:
		    incr=2
		n1,n2=3,num/2
		numRoot = math.sqrt(num)
		while(n1<=n2):
			if (num % n1 == 0):
				n2=num/n1
				factors.append(n1)
				if n1 == n2:
				    break;
				factors.append(n2)
			n1=n1+incr
		return factors
