import json
import web
web.config.debug=True
class Ascending:
		def POST(self):
			outputDic={}
			try:
				inputDic=json.loads(web.data())
				for i in inputDic['numbersList']:
					if type(i) is not int:
						outputDic['status']='ERROR'
						outputDic['error']='Not integer number in the list'
						return outputDic
				outputDic['status']='OK'
				outputDic['numbersList']=self.sortListAsc(inputDic['numbersList'])
			except Exception as e:
				outputDic['status']='ERROR'
				outputDic['error']='Data format is not validate'
			return json.dumps(outputDic)

		def sortListAsc(self, numbersList):
			listN=numbersList
			listN.sort()
			return listN
