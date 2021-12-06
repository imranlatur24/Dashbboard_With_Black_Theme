# -*- encoding: utf-8 -*-
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Employee,new_model
from django.shortcuts import render,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#for csv
import csv,io
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
#for graph
import io,os,csv
import urllib,base64
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import pandas as pd

template = "home/index.html"

@login_required(login_url="/login/")
def index(request):

    # # template_upload = 'home/contact_upload.html'
    # prompt = {
    #     'order': 'Order of the CSV should be x,y'
    # }
    # if request.method == 'GET':
    #     pass
    #     return render(request, template)
    # csv_file = request.FILES['file']
    # print('filename ', csv_file)
    # if not csv_file.name.endswith('.csv'):
    #     messages.error(request, 'uploaded file is not csv type please upload csv file')
    # data_set = csv_file.read().decode('UTF-8')
    #
    # io_string = io.StringIO(data_set)
    # next(io_string)
    # for column in csv.reader(io_string, delimiter=',', quotechar="|"):
    #     _, created = new_model.objects.update_or_create(
    #         X=column[1],
    #         Y=column[2])
    # context = {}
    # return render(request, template, context)
    #for graph
    dataframe=new_model.objects.all()
    dataf =pd.DataFrame(list(new_model.objects.all().values()))
    dataf.to_csv(r'D:/DASHBOARD_DJANGO/django-dashboard-black-master/apps/home/csv/test.csv')
    df = pd.read_csv("D:/DASHBOARD_DJANGO/django-dashboard-black-master/apps/home/csv/test.csv")
    print(df)
    print(type(df))
    dfpage = request.GET.get('page', 1)
    df_paginator = Paginator(dataframe, 5)  # specify here how much record u want to show
    try:
        mydf = df_paginator.page(dfpage)
    except PageNotAnInteger:
        mydf = df_paginator.page(1)
    except EmptyPage:
        mydf = df_paginator.page(df_paginator.num_pages)
    # template
    try:
        X = df.iloc[:, 1:2].values
        y = df.iloc[:, 2].values  # work fine with Position_Salaries and advertising csv file
        print('try block ')
        print('X ', X)
        print('y ', y)
        print('X len ', len(X))
        print('y len ', len(y))
    except IndexError as error:
        print('error ',error)
        # Extracting Independent and dependent Variable
        X = df.iloc[:, 0:1].values #working with sales,data
        y = df.iloc[:, 1:2].values
        print('indexerror block ')
        print('X ', X)
        print('y ', y)
        print('X len ', len(X))
        print('y len ', len(y))
    except Exception as exception:
        print('exception ',exception, False)
        # Extracting Independent and dependent Variable
        X = df.iloc[:, 0:1].values  # working with sales,data
        y = df.iloc[:, 1:2].values
        print('execute except block ')
        print('X ', X)
        print('y ', y)
        print('X len ', len(X))
        print('y len ', len(y))
    finally:
        print('finally block')
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X,
                                                            y,
                                                            test_size=0.33,  # update
                                                            random_state=51)
        poly1 = PolynomialFeatures(degree=1)
        X_poly1 = poly1.fit_transform(X)
        poly1.fit(X_poly1, y)
        lin1 = LinearRegression()

        lin1.fit(X_poly1, y)
        co = lin1.coef_
        deg1_x0 = co[0]
        deg1_x1 = co[1]
        print('coefficient 1-', deg1_x0)
        print('coefficient 2-', deg1_x1)
        # lin1.fit(X_poly1.reshape(1, -1), y)
        # Predicting a new result with Linear Regression
        # print('degree-1 prediction ',lin1.predict(110))
        deg1_const = lin1.intercept_
        deg1_acc = lin1.score(poly1.fit_transform(X_test), y_test)
        print('Accuracy Score:', deg1_acc)
        print('Intercept :', deg1_const)

        plt.scatter(X, y, color='blue')
        plt.plot(X, lin1.predict(poly1.fit_transform(X)), '-', label='Degree-1')
        plt.title('Polynomial Regression')
        plt.xlabel('Temperature')
        plt.ylabel('Pressure')
        img1 = io.BytesIO()
        plt.savefig(img1, format='png')
        img1.seek(0)
        plot_url1 = base64.b64encode(img1.getvalue()).decode('utf8')

        poly2 = PolynomialFeatures(degree=2)
        X_poly2 = poly2.fit_transform(X)
        poly2.fit(X_poly2, y)
        lin2 = LinearRegression()
        lin2.fit(X_poly2, y)
        # print('degree-2 prediction ', lin2.predict(110))
        co2 = lin2.coef_
        deg2_x0 = co2[0]
        deg2_x1 = co2[1]
        deg2_x2 = co2[2]
        print('co 1 -', deg2_x0)
        print('co 2 -', deg2_x1)
        print('co 3 -', deg2_x2)
        deg2_const = lin2.intercept_
        deg2_acc = lin2.score(poly2.fit_transform(X_test), y_test)
        print('Accuracy Score:', deg2_acc)
        print('Intercept :', deg2_const)

        plt.scatter(X, y, color='blue')
        plt.plot(X, lin2.predict(poly2.fit_transform(X)), '--k', label='Degree-2')
        plt.title('Polynomial Regression')
        plt.xlabel('Temperature')
        plt.ylabel('Pressure')
        img2 = io.BytesIO()
        plt.savefig(img2, format='png')
        img2.seek(0)
        plot_url2 = base64.b64encode(img2.getvalue()).decode('utf8')

        poly3 = PolynomialFeatures(degree=3)
        X_poly3 = poly3.fit_transform(X)
        poly3.fit(X_poly3, y)
        lin3 = LinearRegression()
        lin3.fit(X_poly3, y)
        # print('degree-3 prediction ', lin3.predict(110))
        co = lin3.coef_
        deg3_x0 = co[0]
        deg3_x1 = co[1]
        deg3_x2 = co[2]
        deg3_x3 = co[3]
        print('co 1 -', deg3_x0)
        print('co 2 -', deg3_x1)
        print('co 3 -', deg3_x2)
        print('co 4 -', deg3_x3)
        deg3_const = lin3.intercept_
        deg3_acc = lin3.score(poly3.fit_transform(X_test), y_test)
        print('Accuracy Score:', deg3_acc)
        print('Intercept :', deg3_const)
        plt.scatter(X, y, color='blue')
        plt.plot(X, lin3.predict(poly3.fit_transform(X)))
        plt.title('Polynomial Regression')
        plt.xlabel('Temperature')
        plt.ylabel('Pressure')
        img3 = io.BytesIO()
        plt.savefig(img3, format='png')
        img3.seek(0)
        plot_url3 = base64.b64encode(img3.getvalue()).decode('utf8')

        poly = PolynomialFeatures(degree=4)
        X_poly = poly.fit_transform(X)
        poly.fit(X_poly, y)
        lin4 = LinearRegression()
        lin4.fit(X_poly, y)
        # print('degree-4 prediction ', lin4.predict(110))
        co4 = lin4.coef_
        print('Coefficient ', co4)
        deg4_x0 = co4[0]
        deg4_x1 = co4[1]
        deg4_x2 = co4[2]
        deg4_x3 = co4[3]
        deg4_x4 = co4[4]
        print('co 1 -', deg4_x0)
        print('co 2 -', deg4_x1)
        print('co 3 -', deg4_x2)
        print('co 4 -', deg4_x3)
        print('co 5 -', deg4_x4)
        deg4_const = lin4.intercept_
        deg4_acc = lin4.score(poly.fit_transform(X_test), y_test)
        print('Accuracy Score:', deg4_acc)
        print('Intercept :', deg4_const)
        img = io.BytesIO()  ################
        plt.scatter(X, y, color='blue')
        plt.plot(X, lin4.predict(poly.fit_transform(X)), '-*', color='red', label='Degree-4')
        plt.title('Polynomial Regression')
        plt.xlabel('Temperature')
        plt.ylabel('Pressure')
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')
        #pagination
        context = {'segment': 'index'}
        queryset = Employee.objects.all().order_by('name')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 5)  # specify here how much record u want to show
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        if request.method == 'GET':
            return render(request, template,
                          {'users': users, 'dataframe': mydf,
                           'deg1_acc':deg1_acc,'deg1_const':deg1_const,
                           'deg2_acc':deg2_acc,'deg2_const':deg2_const,
                           'deg3_acc':deg3_acc,'deg3_const':deg3_const,
                           'deg4_acc':deg4_acc,'deg4_const':deg4_const,
                           'deg4': plot_url, 'deg3': plot_url3, 'deg2': plot_url2,
                           'deg1': plot_url1})
        csv_file = request.FILES['file']
        print('filename ', csv_file)
        csv_file = request.FILES['file']
        print('filename ', csv_file)
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'uploaded file is not csv type please upload csv file')
        data_set = csv_file.read().decode('UTF-8')
        print('dataset in upload ', data_set)
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            _, created = new_model.objects.update_or_create(
                X=column[1],
                Y=column[2])
        context = {}
        return render(request, template,
                      {'users': users,'dataframe':mydf,
                       'deg1_acc':deg1_acc,'deg1_const':deg1_const,
                       'deg2_acc': deg2_acc, 'deg2_const': deg2_const,
                       'deg3_acc': deg3_acc, 'deg3_const': deg3_const,
                       'deg4_acc': deg4_acc, 'deg4_const': deg4_const,
                       'deg4': plot_url, 'deg3': plot_url3, 'deg2': plot_url2, 'deg1': plot_url1},context)

    #datepicker from-to
    # if request.method=="POST":
    #     fromdate=request.POST.get('from_date')
    #     todate=request.POST.get('to_date')
    #     searchresult=Employee.objects.raw('SELECT id, name, country, city, salary, created_at FROM home_employee WHERE created_at BETWEEN "'+fromdate+'" AND "'+todate+'"')
    #     print('search result ',searchresult)
    #     page = request.GET.get('page', 1)
    #     paginator = Paginator(searchresult, 5)  # specify here how much record u want to show
    #     try:
    #         users = paginator.page(page)
    #     except PageNotAnInteger:
    #         users = paginator.page(1)
    #     except EmptyPage:
    #         users = paginator.page(paginator.num_pages)
    #     return render(request,"home/index.html",{'users':users})
    # else:
    #     queryset = Employee.objects.all().order_by('name')
    #     page = request.GET.get('page', 1)
    #     paginator = Paginator(queryset, 5)  # specify here how much record u want to show
    #     try:
    #         users = paginator.page(page)
    #     except PageNotAnInteger:
    #         users = paginator.page(1)
    #     except EmptyPage:
    #         users = paginator.page(paginator.num_pages)
    #     return render(request,"home/index.html",{'users': users,'deg4':plot_url,'deg3':plot_url3,'deg2':plot_url2,'deg1':plot_url1})

@permission_required('admin.can_add_log_entry')
def upload_csv(request): # ref link https://www.myhsts.org/upload-and-process-website-cvs-file-using-python-django.html
    template='home/contact_upload.html'
    prompt = {
        'order': 'Order of the CSV should be x,y'
    }
    if request.method == 'GET':
        return render(request, template)
    csv_file=request.FILES['file']
    print('filename ',csv_file)
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'uploaded file is not csv type please upload csv file')
    data_set = csv_file.read().decode('UTF-8')
    print('dataset in upload ',data_set)
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = new_model.objects.update_or_create(
            X=column[1],
            Y=column[2])
    context = {}
    messages.success(request,"csv file successfully uploaded into databases")
    return redirect(template,context)

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
