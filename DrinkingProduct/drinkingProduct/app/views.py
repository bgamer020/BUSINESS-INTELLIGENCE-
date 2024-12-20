# Create your views here.
from django.shortcuts import render
from .forms import Form1, Form2, Form3, Form4, Form5
import os
import csv
from django.conf import settings
from math import sqrt
import csv
import os
from django.conf import settings
from django.shortcuts import render
from .forms import Form1  # Nhớ import form của bạn

def euclidean_distance(input_data, row_data):
    print(input_data)
    print(row_data)
    # Hàm tính khoảng cách Euclidean giữa hai danh sách
    return float(sum((x - y) ** 2 for x, y in zip(input_data, row_data)) ** 0.5)

import csv
import os
from django.conf import settings

def view1(request):
    form = Form1()
    nearest_row = None
    min_distance = float('inf')
    headers = []
    result_data = []
    products = []

    if request.method == "POST":
        form = Form1(request.POST)
        if form.is_valid():
            input_vi = form.cleaned_data['vi']
            input_data = [
                form.cleaned_data['nang_luong'],
                form.cleaned_data['hydrat_carbon'],
                form.cleaned_data['chat_dam'],
                form.cleaned_data['chat_beo'],
                form.cleaned_data['cynarin'],
                form.cleaned_data['vitamin_c'],
                form.cleaned_data['natri'],
                form.cleaned_data['ti_le_tao'],
                form.cleaned_data['ti_le_luu'],
                form.cleaned_data['ti_le_cam'],
                form.cleaned_data['ti_le_nuoc_ep'],
                form.cleaned_data['ti_le_nho'],
                form.cleaned_data['ti_le_oi'],
                form.cleaned_data['ti_le_kiwi'],
                form.cleaned_data['ti_le_dao'],
                form.cleaned_data['egcg'],
                form.cleaned_data['polyphenol'],
                form.cleaned_data['l_theanin'],
            ]

            csv_path = os.path.join(settings.BASE_DIR, 'app/static/app/datasets/DinhDuongNuocGiaiKhat.csv')
            with open(csv_path, 'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader)  # Lấy tiêu đề

                col_indices = [
                    headers.index('Năng lượng (kcal)'),
                    headers.index('Hydrat carbon (g)'),
                    headers.index('Chất đạm (g)'),
                    headers.index('Chất béo (g)'),
                    headers.index('Cynarin (g)'),
                    headers.index('Vitamin C (mg)'),
                    headers.index('Natri (mg)'),
                    headers.index('Tỉ lệ nước ép táo cô đặc'),
                    headers.index('Tỉ lệ nước ép lựu cô đặc'),
                    headers.index('Tỉ lệ nước ép cam cô đặc'),
                    headers.index('Tỉ lệ nước ép'),
                    headers.index('Tỉ lệ nước ép nho cô đặc'),
                    headers.index('Tỉ lệ nước ép ổi cô đặc'),
                    headers.index('Tỉ lệ nước ép kiwi cô đặc'),
                    headers.index('Tỉ lệ nước ép đào cô đặc'),
                    headers.index('EGCG (mg)'),
                    headers.index('Polyphenol (mg)'),
                    headers.index('L-Theanin (mg)'),
                ]

                # Duyệt qua từng dòng và tính khoảng cách
                for row in reader:
                    if row[1] == input_vi:
                        row_data = [float(row[i]) for i in col_indices]

                        distance = euclidean_distance(input_data, row_data)
                        if distance < min_distance:
                            min_distance = distance
                            nearest_row = row

            # Kết hợp header và giá trị của nearest_row thành một danh sách các tuple
            result_data = zip(headers, nearest_row) if nearest_row else []

            # Bước 2: Dùng tên sản phẩm từ nearest_row để tìm các sản phẩm trong dataset.csv
            if nearest_row:
                product_name = nearest_row[0]  # Giả sử tên sản phẩm ở cột đầu tiên của nearest_row

                # Đọc dataset.csv và tìm các sản phẩm có tên giống với tên trong nearest_row
                dataset_path = os.path.join(settings.BASE_DIR, 'app/static/app/datasets/dataset.csv')
                with open(dataset_path, 'r', encoding='utf-8') as dataset_file:
                    dataset_reader = csv.DictReader(dataset_file)

                    # Tìm các sản phẩm có tên trùng với product_name
                    products = [row for row in dataset_reader if product_name.lower() in row['detail_product'].lower()]

    return render(request, "view1.html", {
        "form": form,
        'result_data': result_data,
        'products': products
    })


# ---------------------------------------- SEPERATE -------------------------- #


def view2(request):
    form = Form2()
    nearest_row = None
    min_distance = float('inf')
    headers = []
    result_data = []
    products = []

    if request.method == "POST":
        form = Form2(request.POST)
        if form.is_valid():
            input_label = form.cleaned_data['label']
            input_data = [
                form.cleaned_data['natri'],
                form.cleaned_data['kali'],
                form.cleaned_data['clorid'],
                form.cleaned_data['calci'],
                form.cleaned_data['phospho'],
                form.cleaned_data['magnesi'],
                form.cleaned_data['mangan'],
                form.cleaned_data['sat'],
                form.cleaned_data['iot'],
                form.cleaned_data['kem'],
                form.cleaned_data['dong'],
                form.cleaned_data['selen'],
                form.cleaned_data['vitamin_a'],
                form.cleaned_data['vitamin_d3'],
                form.cleaned_data['vitamin_e'],
                form.cleaned_data['vitamin_k1'],
                form.cleaned_data['vitamin_c'],
                form.cleaned_data['vitamin_b1'],
                form.cleaned_data['vitamin_b2'],
                form.cleaned_data['niacin'],
                form.cleaned_data['vitamin_b6'],
                form.cleaned_data['acid_folic'],
                form.cleaned_data['acid_pantothetic'],
                form.cleaned_data['vitamin_b12'],
                form.cleaned_data['biotin'],
                form.cleaned_data['cholin'],
                form.cleaned_data['vitamin_k2'],
                form.cleaned_data['acid_linoleic'],
                form.cleaned_data['acid_alpha_linolenic'],
                form.cleaned_data['ara'],
                form.cleaned_data['dha'],
                form.cleaned_data['acid_oleic'],
                form.cleaned_data['pufa'],
                form.cleaned_data['mufa'],
                form.cleaned_data['mct'],
                form.cleaned_data['nang_luong'],
                form.cleaned_data['chat_dam'],
                form.cleaned_data['tryptophan'],
                form.cleaned_data['chat_beo'],
                form.cleaned_data['hydrat_cacbon'],
                form.cleaned_data['chat_xo_hoa_tan'],
                form.cleaned_data['gos'],
                form.cleaned_data['fl'],
                form.cleaned_data['taurin'],
                form.cleaned_data['inositol'],
                form.cleaned_data['l_carnitin'],
                form.cleaned_data['nucleotid'],
                form.cleaned_data['lutein'],
                form.cleaned_data['do_am'],
                form.cleaned_data['bifidobacterium'],
                form.cleaned_data['lactobacillus_rhamnosus'],
                form.cleaned_data['lysin'],
                form.cleaned_data['beta_caroten'],
                form.cleaned_data['collagen'],
                form.cleaned_data['molybden'],
                form.cleaned_data['vitamin_pp'],
                form.cleaned_data['crom'],
                form.cleaned_data['phosphatidylserine'],
                form.cleaned_data['vitamin_b9'],
                form.cleaned_data['vitamin_b5'],
                form.cleaned_data['canxi'],
                form.cleaned_data['cholesterol'],
                form.cleaned_data['vitamin_b3'],
            ]

            csv_path = os.path.join(settings.BASE_DIR, 'app/static/app/datasets/DinhDuongSuaBot.csv')
            with open(csv_path, 'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader)  # Lấy tiêu đề

                label_index = headers.index('Label')  # Giả sử trường 'Label' tồn tại
                col_indices = list(range(2, len(headers))) # Lấy tất cả các cột
                
                # Duyệt qua từng dòng và tính khoảng cách nếu label khớp
                for row in reader:                    
                    if row[label_index] == input_label:  # Kiểm tra label khớp
                        row_data = [float(row[i]) if row[i] != '' else 0 for i in col_indices if i != label_index]   # Loại bỏ cột Label
                        distance = euclidean_distance(input_data, row_data)
                        if distance < min_distance:
                            min_distance = distance
                            nearest_row = row

            # Kết hợp header và giá trị của nearest_row thành một danh sách các tuple
            result_data = zip(headers, nearest_row) if nearest_row else []

            # Bước 2: Dùng tên sản phẩm từ nearest_row để tìm các sản phẩm trong dataset
            if nearest_row:
                product_name = nearest_row[0]  # Giả sử tên sản phẩm ở cột đầu tiên của nearest_row

                dataset_path = os.path.join(settings.BASE_DIR, 'app/static/app/datasets/dataset.csv')
                with open(dataset_path, 'r', encoding='utf-8') as dataset_file:
                    dataset_reader = csv.DictReader(dataset_file)

                    # Tìm các sản phẩm có tên trùng với product_name
                    products = [row for row in dataset_reader if product_name.lower() in row['detail_product'].lower()]
                    print(products)

    return render(request, "view2.html", {
        "form": form,
        'result_data': result_data,
        'products': products
    })



# ---------------------------------------- SEPERATE -------------------------- #

def view3(request):
    form = Form3()
    nearest_row = None
    min_distance = float('inf')
    headers = []
    result_data = []
    products = []


    if request.method == "POST":
        form = Form3(request.POST)
        if form.is_valid():
            # Xử lý dữ liệu ở đây
            input_loai_men = form.cleaned_data['Loai_Men']
            input_vi = form.cleaned_data['Vi']
            input_data = [
                form.cleaned_data['Nang_luong'],
                form.cleaned_data['Hydrat_carbon'],
                form.cleaned_data['Chat_dam'],
                form.cleaned_data['Chat_beo'],
                form.cleaned_data['Ti_le_sua_tuoi'],
                form.cleaned_data['Ti_le_nha_dam'],
                form.cleaned_data['Ti_le_mut_trai_cay'],
                form.cleaned_data['Collagen'],
                form.cleaned_data['Ti_le_mut_luu'],
                form.cleaned_data['Ti_le_thach_dua'],
                form.cleaned_data['Ti_le_nep_cam'],
                form.cleaned_data['Ti_le_tran_chau_duong_den'],
                form.cleaned_data['Ti_le_mut_dau'],
                form.cleaned_data['Ti_le_mut_viet_quat'],
                form.cleaned_data['Ti_le_mut_la_dua'],
                form.cleaned_data['Ti_le_sua_bot_tach_beo'],
                form.cleaned_data['Ti_le_sua_chua_len_men_tu_nhien'],
                form.cleaned_data['Calci'],
                form.cleaned_data['Natri'],
                form.cleaned_data['Lysin'],
                form.cleaned_data['Kenm'],
                form.cleaned_data['Magie'],
                form.cleaned_data['Axit_Folic'],
                form.cleaned_data['Vitamin_D3'],
                form.cleaned_data['Vitamin_A'],
                form.cleaned_data['Vitamin_B1'],
                form.cleaned_data['Vitamin_B6'],
                form.cleaned_data['Vitamin_B9'],
                form.cleaned_data['Vitamin_B12'],
                form.cleaned_data['Vitamin_B3'],
                form.cleaned_data['Vitamin_B2'],
                form.cleaned_data['Ti_le_ngu_goc_cacao'],
            ]

            csv_path = os.path.join(settings.BASE_DIR, 'app/static/app/datasets/DinhDuongSuaChuaAn.csv')
            with open(csv_path, 'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader)  # Lấy tiêu đề

                col_indices = list(range(4, len(headers)))
                loai_men_index = headers.index('Loại Men')
                vi_index = headers.index('Vị')

                for row in reader:
                    if row[loai_men_index] == input_loai_men and row[vi_index] == input_vi:
                        row_data = [float(row[i]) if row[i] != '' else 0 for i in col_indices]
                        distance = euclidean_distance(input_data, row_data)
                        if distance < min_distance:
                            min_distance = distance
                            nearest_row = row

                result_data = zip(headers, nearest_row) if nearest_row else []

                if nearest_row:
                    product_name = nearest_row[0]  # Giả sử tên sản phẩm ở cột đầu tiên
                    dataset_path = os.path.join(settings.BASE_DIR, 'app/static/app/datasets/dataset.csv')
                    with open(dataset_path, 'r', encoding='utf-8') as dataset_file:
                        dataset_reader = csv.DictReader(dataset_file)
                        products = [row for row in dataset_reader if product_name.lower() in row['detail_product'].lower()]


    return render(request, "view3.html", {
        "form": form,
        "result_data": result_data,
        "products": products
    })


# ---------------------------------------- SEPERATE -------------------------- #


def view4(request):

    form = Form4()
    nearest_row = None
    min_distance = float('inf')
    headers = []
    result_data = []
    products = []

    if request.method == "POST":
        form = Form4(request.POST)
        if form.is_valid():
            # Lấy dữ liệu từ form
            input_loai_men = form.cleaned_data['Loai_Men']
            input_data = [
                form.cleaned_data[field_name]
                for field_name in form.fields
                if field_name != 'Loai_Men'
            ]
        csv_path = os.path.join(settings.BASE_DIR, 'app/static/app/datasets/DinhDuongSuaChuaNuoc.csv')
        with open(csv_path, 'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader)  # Lấy tiêu đề
                
                # Xác định cột cần so sánh
                col_indices = list(range(4, len(headers)))  # Cột dinh dưỡng bắt đầu từ cột thứ 4
                loai_men_index = headers.index('Loại Men')

                # Tìm dòng có khoảng cách gần nhất
                for row in reader:
                    if row[loai_men_index] == input_loai_men:
                        row_data = [float(row[i]) if row[i] != '' else 0 for i in col_indices]
                        distance = euclidean_distance(input_data, row_data)
                        if distance < min_distance:
                            min_distance = distance
                            nearest_row = row

                result_data = zip(headers, nearest_row) if nearest_row else []

                # Tìm sản phẩm liên quan
                if nearest_row:
                    product_name = nearest_row[0]  # Giả sử tên sản phẩm ở cột đầu tiên
                    dataset_path = os.path.join(settings.BASE_DIR, 'app/static/app/datasets/dataset.csv')
                    with open(dataset_path, 'r', encoding='utf-8') as dataset_file:
                        dataset_reader = csv.DictReader(dataset_file)
                        products = [row for row in dataset_reader if product_name.lower() in row['detail_product'].lower()]

    return render(request, "view4.html", {
        "form": form,
        "result_data": result_data,
        "products": products
    })

# ---------------------------------------- SEPERATE -------------------------- #

# View 5: Hiển thị dữ liệu từ dataset2.csv
def view5(request):
    form = Form5()
    nearest_row = None
    min_distance = float('inf')
    headers = []
    result_data = []
    products = []

    if request.method == "POST":
        form = Form5(request.POST)
        if form.is_valid():
            # Lấy dữ liệu từ form
            input_flavor = form.cleaned_data['Flavor']
            input_data = [
                form.cleaned_data[field_name]
                for field_name in form.fields
                if field_name != 'Flavor'
            ]
            
            # Đường dẫn tới file CSV chứa dữ liệu dinh dưỡng
            csv_path = os.path.join(settings.BASE_DIR, 'app/static/app/datasets/DinhDuongSuaNuoc.csv')
            with open(csv_path, 'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader)  # Lấy tiêu đề
                
                # Xác định cột cần so sánh (các cột dinh dưỡng)
                col_indices = list(range(1, len(headers) - 1 ))  # Cột dinh dưỡng bắt đầu từ cột thứ 4
                flavor_index = headers.index('flavor') 

                # Tìm dòng có khoảng cách gần nhất
                for row in reader:
                    if row[flavor_index] == input_flavor:
                        row_data = [float(row[i]) if row[i] != '' else 0 for i in col_indices]
                        distance = euclidean_distance(input_data, row_data)
                        if distance < min_distance:
                            min_distance = distance
                            nearest_row = row

                result_data = zip(headers, nearest_row) if nearest_row else []

                # Tìm sản phẩm liên quan
                if nearest_row:
                    product_name = nearest_row[0]  # Giả sử tên sản phẩm ở cột đầu tiên
                    dataset_path = os.path.join(settings.BASE_DIR, 'app/static/app/datasets/dataset.csv')
                    with open(dataset_path, 'r', encoding='utf-8') as dataset_file:
                        dataset_reader = csv.DictReader(dataset_file)
                        products = [row for row in dataset_reader if product_name.lower() in row['detail_product'].lower()]

    return render(request, "view5.html", {
        "form": form,
        "result_data": result_data,
        "products": products
    })