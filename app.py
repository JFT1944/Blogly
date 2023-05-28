"""Blogly application."""

from flask import Flask, render_template, session, redirect, request
# from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, PostTag, Tag
import datetime

app = Flask(__name__)


app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'cows'
# DEBUG_TB_INTERCEPT_REDIRECTS = False
# toolbar = DebugToolbarExtension(app)


# ----------------------------------------------------------------------

# ********************* : To Do : **********************************
# 1. Get posts to add tags with them.
# 2. Show posts on tag page with .query.all()
# 3. Show tags under the posts 
# 4. Make the homepage the final that shows all of the different posts from different people.
# 5. Write tests for all get and post routes

# ----------------------------------------------------------------------



connect_db(app)
app.app_context().push()
# db.create_all()

@app.route('/')
def home():
    return redirect('/users')


@app.route('/users')
def users():
    total = []
    currentusers = User.query.all()
    for user in currentusers:
        u = []
        u.append(user.first_name)
        u.append(user.last_name)
        u.append(user.image_url)
        u.append(user.id)
        total.append(u)
        print(total)
    return render_template('user.html', total=total)
# , total=total

@app.route('/users/<int:userid>')
def userId(userid):
    try:

        top = []
    # bignum = int(userid)
        print(f'############################{userid}############################')
        print('print above')


    

        id=int(userid)
        userpage = User.query.get(id)
        
        print(f'##############################{userpage}#################################')
        userposts = Post.query.filter_by(user_key=id)
        print(f'##############################userpost{userposts.id}#################################')
    except:

        print('did not work')
    # userposts = Post.query.filter_by(user_key=id)
    # print(userposts)
    # print(userpage[0])
    # for user in userpage:
    #     top.append(user[0])
    #     top.append(user[1])
    #     top.append(user[2])
    #     print(top)
    return render_template('user_page.html', userpage=userpage, userposts=userposts, id=id)
# posts=userposts | id=id

@app.route('/users/new', methods=['POST', 'GET'])
def newUser():
    if request.method == 'POST':
        print('this was a post request')
        firname = request.form['f_name']
        print(firname)
        lasname = request.form['l_name']
        print(lasname)
        imgurl = request.form['img_url']
        
        newUser = User(first_name=firname, last_name=lasname, image_url=imgurl)
        db.session.add(newUser)
        db.session.commit()
        
        return redirect('/users')

    else:
        return render_template('new-user-form.html')


@app.route('/users/<userid>/edit', methods=['POST', 'GET'])
def user_id_edit(userid):
    if request.method == 'POST':
        return 'Your info has been changed!'
    else:
        top = []
        id=int(userid)
        userpage = User.query.get(id)
        top.append(userpage.first_name)
        top.append(userpage.last_name)
        top.append(userpage.image_url)
        # top.append(userpage.id)
        print (top)
        return render_template('user_edit.html', top=top) 

        # ------------------------Posts------------------------
        # ------------------------Posts------------------------
        # ------------------------Posts------------------------
        # ------------------------Posts------------------------
        # ------------------------Posts------------------------
        # ------------------------Posts------------------------
        # ------------------------Posts------------------------
        # ------------------------Posts------------------------
        # ------------------------Posts------------------------

@app.route('/users/<userid>/posts/new', methods=['POST', 'GET'])
def making_posts(userid):
    if request.method == 'POST':
        print('this was a post request')
        title = request.form['title']
        print(title)
        content = request.form['content']
        print(content)
        dati = [datetime.date, datetime.time]
        print(dati)
        posttags = Tag.query.all()
        print(int(len(posttags)))
        # for postnum in range(int(len(posttags))):
        all_tags_checked = []
        for postnum in posttags:
            
            # postnum = postnum + 1
            print(int(postnum.id))
            try:
                newnum = int(postnum.id)
                newnum = request.form[f'sillyTags{postnum.id}']
                all_tags_checked.append(int(postnum.id))
                print(postnum.id)

            except:
                print('Didn"t work')
        # stags = request.form['sillyTags']
        # print(stags)
        # ---
        print(f'''
        ######################################################################
        
        {all_tags_checked}
        
        ######################################################################
        ''')
        # tags = Tag.query.all()
        
        # tgall = []
        # for t in tags:
        #     tgall.append(t.title)
        #     print(tgall)
        # for i in tgall:
        #     i = request.form[f'{i}']
        #     print(i)

        newPost = Post(title=title, content=content, created_at=f'{dati[0]} / {dati[1]}', user_key=userid)
        
        db.session.add(newPost)
        db.session.commit()

        find_post = Post.query.filter_by(title=newPost.title, content=newPost.content).first()
        print(find_post)
        for tg in all_tags_checked:
            tg = PostTag(post_id=find_post.id, tag_id=tg)
            db.session.add(tg)
        db.session.commit()


        return redirect(f'/users/{userid}')
    else:
        tags = Tag.query.all()
        return render_template('new_post_page.html', tags=tags)

@app.route('/posts/<int:postid>')
def unit_post(postid):
    id = int(postid)
    singlepost = Post.query.get(id)
    posttags = PostTag.query.filter_by(post_id=postid).all()
    print(posttags)
    all_the_tags = []
    for post in posttags:
        print(f'****************Post:{type(post)}*************************')
        newTags = Tag.query.get(post.tag_id)
        print(f'****************Tag:{type(newTags)}*************************')
        all_the_tags.append(newTags)
    print(f'All the Tags:{all_the_tags}')
    return render_template('post-page.html', singlepost=singlepost, tags=all_the_tags)

@app.route('/posts/<int:postid>/edit', methods=['POST', 'GET'])
def unit_post_edit(postid):
    if request.method == 'POST':
        print('this was a post request')
        title = request.form['title']
        print(title)
        content = request.form['content']
        print(content)
        findpost = Post.query.get(postid)
        print(f'####################{findpost}######################')
        if title != "":
            findpost.title = title
        if content != "":
            findpost.content = content
        
        db.session.add(findpost)
        db.session.commit()
        return redirect(f'/users/{findpost.user_key}')
    
    else:
        id = int(postid)
        singlepost = Post.query.get(id)
    

    return render_template('post-edit.html', id=id, singlepost=singlepost)

@app.route('/posts/<int:postid>/delete', methods=['POST', 'GET'])
def delete_post(postid):
    if request.method == 'POST':
        decision = request.form['deleting']
        findpost = Post.query.get(postid)
        if decision == 'yes':
            print(f'*****************{findpost}*****************')
            Post.query.filter_by(id=postid).delete()


            db.session.commit()
        return redirect(f'/users/{findpost.user_key}')

    return render_template('post-delete.html')



# ------------------------tags------------------------
# ------------------------tags------------------------
# ------------------------tags------------------------
# ------------------------tags------------------------
# ------------------------tags------------------------
# ------------------------tags------------------------
# ------------------------tags------------------------

@app.route('/tags')
def tags():
    tagslist = Tag.query.all()



    return render_template('tag_page.html', tagslist=tagslist)

@app.route('/tags/<int:tagid>')
def single_tags(tagid):

    ThisTag = Tag.query.get(tagid)
    print(f'''*******************{ThisTag}**********************''')
    post_tags = PostTag.query.filter_by(tag_id=tagid).all()
    print(f'''*******************Post Tags:{post_tags}**********************''')
    all_posts = []
    for posts in post_tags:
        newpost = Post.query.get(posts.post_id)
        all_posts.append(newpost)
    print(f'''*******************{all_posts}**********************''')
    return render_template('tag.html', ThisTag=ThisTag, posts=all_posts)
    
@app.route('/tags/new', methods=['POST', 'GET'])
def new_tags():
    if request.method == 'POST':
        NewTagName = request.form['nt']
        ntn = Tag(title=NewTagName)
        db.session.add(ntn)
        db.session.commit()
        return redirect('/tags')

    return render_template('tag_new.html')

@app.route('/tags/<int:tagid>/edit', methods=['POST', 'GET'])
def edit_tags(tagid):
    ThisTag = Tag.query.get(tagid)
    if request.method == 'POST':
        print('this is a post')
        NewTagName = request.form['nt']
        print(f'**************{NewTagName}*******************')
        ThisTag.title = NewTagName
        print(f'**************{ThisTag.title}*******************')
        db.session.add(ThisTag)
        db.session.commit()
        return redirect('/tags')
    # return render_template('tag.html', ThisTag=ThisTag)
    return render_template('tag_edit.html', ThisTag=ThisTag )

@app.route('/tags/<int:tagid>/delete', methods=['POST', 'Get'])
def delete_tags(tagid):
    if request.method == 'POST':
        decision = request.form['deleting']
        print(f'****************{decision}**********************')
        tagged = Tag.query.get(tagid)
        if decision == 'yes':
            # print(f'*****************{findpost}*****************')
            Tag.query.filter_by(id=tagid).delete()
            db.session.commit()
        return redirect('/tags')

    else:
        return render_template('tag_delete.html')
