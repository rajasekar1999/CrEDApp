from flask import Flask, render_template, request,redirect,url_for
import dbops

app = Flask(__name__, template_folder='templates')

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/created', methods = ['GET','POST'])
def created():
    if request.method == 'POST':
        result = request.form.to_dict()
        form = [result['title'],result['content'],result['citation']]
        print(dbops.ListContent(form))
        return redirect(url_for('Home'))

@app.route('/edit')
def editselect():
    li = dbops.getList()
    li = [str(i)[2:-3] for i in li]
    return render_template('editselect.html',lis=li)

@app.route('/editview', methods=['POST','GET'])
def edit():
        if request.method == 'POST':
            result = request.form.to_dict()
            title = result['index']
            title = str(title)
            print(title)
            res = dbops.FetchEdit(title)
            print(res)
            return render_template('edit.html',res = res)

@app.route('/delete')
def delete():
    li = dbops.getList()
    li = [str(i)[2:-3] for i in li]
    return render_template('deleteselect.html',lis=li)

@app.route('/deleted',methods=['POST','GET'])
def deleted():
    if request.method == 'POST':
        result = request.form.to_dict()
        if result['deleteall'] == 'on':
            dbops.DeleteAll()
        else:
            dbops.DeleteContent(result['index'])
        return redirect(url_for('Home'))

@app.route('/update',methods=['POST','GET'])
def update():
    if request.method == 'POST':
        result = request.form.to_dict()
        print(result)
        form = [result['title'],result['content'],result['citation']]
        print(dbops.UpdateContent(form))
        return redirect(url_for('Home'))
        
@app.route('/view')
def view():
    li = dbops.getList()
    li = [str(i)[2:-3] for i in li]
    return render_template('viewarticles.html', lis=li)

@app.route('/display',methods=['GET','POST'])
def display():
    if request.method == 'POST':
        result = request.form.to_dict()
        key = result['index']
        res = dbops.FetchArticle(key)
        return render_template('displayarticles.html',res=res)

if __name__ == '__main__':
    app.run(debug=True)
