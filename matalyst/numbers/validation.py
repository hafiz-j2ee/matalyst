import json
import web
web.config.debug=True

class IsInteger:
	def POST(self):
		data=web.data()
		numDic=json.loads(data)
		return 	json.dumps(self.checkNumber(numDic))
 	def checkNumber(self, numDic):
		outputDic={}
		if numDic.has_key('number'):
			try:
				outputDic['number']=int(numDic['number'].strip())
				outputDic['status']='OK'
			except:
				outputDic['error']="Data is not format correctly"
				outputDic['status']='ERROR'
		else:
			outputDic['error']="Data is not format correctly"
			outputDic['status']='ERROR'
		
		return outputDic
