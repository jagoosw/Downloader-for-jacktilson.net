import urllib.request
import ssl
#Change the values here
start_year = 2006
end_year = 2017
names = ["c1", "c2", "m1"] #Put the paper names you want here
store = "/Users/John/Maths/Papers"#Put the directory you want the papers in here
#Do not modify from here down

context = ssl._create_unverified_context()

count_year = start_year

general_paper = "https://jacktilson.net/edu/maths/pastpapers/"
general_ms = "https://jacktilson.net/edu/maths/markschemes/summer-"

while count_year <= end_year:
	ms_url = general_ms+str(count_year)+".pdf"
	ms_data =  (urllib.request.urlopen(ms_url, context=context)).read()
	print(str(count_year)+ " MS")
	with open(store"Markschemes/"+str(count_year)+".pdf", "wb") as file:
		file.write(ms_data)

	for paper in names:
		paper_url = general_paper+paper+"/"+paper+"-june-"+str(count_year)+".pdf"
		paper_data = (urllib.request.urlopen(paper_url, context=context)).read()
		print(str(count_year)+ paper)
		with open(store+paper+"/"+str(count_year)+".pdf", "wb") as file:  
			file.write(paper_data)
	
	print(str(count_year)+" done...")
	count_year+=1