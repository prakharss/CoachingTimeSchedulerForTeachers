#Attendance Module pdf and excel report generation.


#To generate the excel files, install xlsxwriter 
sudo pip install XlsxWriter


#To generate pdf files, install reportlab and its library platypus
#(Generally it comes installed along with python)

#Use the following command if not installed
pip install reportlab

#If already installed but not the latest version, use the following command
pip install reportlab --upgrade

pip install pillow

sudo apt-get install python-xlrd

sudo apt-get install python-pdfrw

sudo pip install pdfkit

sudo apt-get install wkhtmltopdf

#Install pymongo for fetching marks from iitbombayx
python -m pip install pymongo
