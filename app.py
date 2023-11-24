#-----------------------
# 匯入Flask類別
#-----------------------
from flask import Flask, render_template

#-----------------------
# 產生一個Flask物件
# 名稱為app
#-----------------------
app = Flask(__name__)

#-----------------------
# 用裝飾器定義app的路由
#-----------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customer/test')
def customer_test():
    '''
    data = {}
    data['name'] = "石小凱"
    data['gender'] = "男"
    '''
    data = {'name':'石凱', 'gender':'男', 'age':23}
    
    return render_template('test.html', data = data)

@app.route('/customer/list')
def customer_list():

    data = [{'name':'石凱', 'gender':'男', 'age':23},
            {'name':'黃子弘凡', 'gender':'男', 'age':24},
            {'name':'唐九洲', 'gender':'男', 'age':25},
            {'name':'齊思鈞', 'gender':'男', 'age':29},
            {'name':'蒲熠星', 'gender':'男', 'age':29}]
    
    return render_template('list.html', data = data)
#-----------------------
# 執行app
#-----------------------
if __name__ == '__main__':
    app.run(port=5000, debug = True)