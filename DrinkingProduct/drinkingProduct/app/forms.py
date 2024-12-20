from django import forms
from django.core.exceptions import ValidationError

def validate_positive(value):
    if value < 0:
        raise ValidationError("Giá trị không được âm.")

class Form1(forms.Form):

    
    vi_list = [
    ("Cam", "Cam"),
    ("Nho", "Nho"),
    ("Táo", "Táo"),
    ("Ổi Ruột Hồng", "Ổi Ruột Hồng"),
    ("Lựu - Táo", "Lựu - Táo"),
    ("Đào", "Đào"),
    ("Kiwi - Táo", "Kiwi - Táo"),
    ("Trà đào", "Trà đào"),
    ("Trà vải", "Trà vải"),
    ("Trà chanh", "Trà chanh"),
    ("Trà ô long", "Trà ô long"),
    ("Táo đào", "Táo đào"),
    ]

    vi = forms.ChoiceField(
        label="Chọn vị",
        choices= vi_list,
        widget=forms.Select(attrs={"class": "form-control"}),  # Thêm class CSS nếu cần
    )

    nang_luong = forms.FloatField(label='Năng lượng (kcal)', required=True, initial=0, 
        validators=[validate_positive])
    hydrat_carbon = forms.FloatField(label='Hydrat carbon (g)', required=True, initial=0, 
        validators=[validate_positive])
    chat_dam = forms.FloatField(label='Chất đạm (g)', required=True, initial=0, 
        validators=[validate_positive])
    chat_beo = forms.FloatField(label='Chất béo (g)', required=True, initial=0, 
        validators=[validate_positive])
    cynarin = forms.FloatField(label='Cynarin (g)', required=True, initial=0, 
        validators=[validate_positive])
    vitamin_c = forms.FloatField(label='Vitamin C (mg)', required=True, initial=0, 
        validators=[validate_positive])
    natri = forms.FloatField(label='Natri (mg)', required=True, initial=0, 
        validators=[validate_positive])
    ti_le_tao = forms.FloatField(label='Tỉ lệ nước ép táo cô đặc', required=True, initial=0, 
        validators=[validate_positive])
    ti_le_luu = forms.FloatField(label='Tỉ lệ nước ép lựu cô đặc', required=True, initial=0, 
        validators=[validate_positive])
    ti_le_cam = forms.FloatField(label='Tỉ lệ nước ép cam cô đặc', required=True, initial=0, 
        validators=[validate_positive])
    ti_le_nuoc_ep = forms.FloatField(label='Tỉ lệ nước ép', required=True, initial=0, 
        validators=[validate_positive])
    ti_le_nho = forms.FloatField(label='Tỉ lệ nước ép nho cô đặc', required=True, initial=0, 
        validators=[validate_positive])
    ti_le_oi = forms.FloatField(label='Tỉ lệ nước ép ổi cô đặc', required=True, initial=0, 
        validators=[validate_positive])
    ti_le_kiwi = forms.FloatField(label='Tỉ lệ nước ép kiwi cô đặc', required=True, initial=0, 
        validators=[validate_positive])
    ti_le_dao = forms.FloatField(label='Tỉ lệ nước ép đào cô đặc', required=True, initial=0, 
        validators=[validate_positive])
    egcg = forms.FloatField(label='EGCG (mg)', required=True, initial=0, 
        validators=[validate_positive])
    polyphenol = forms.FloatField(label='Polyphenol (mg)', required=True, initial=0, 
        validators=[validate_positive])
    l_theanin = forms.FloatField(label='L-Theanin (mg)', required=True, initial=0, 
        validators=[validate_positive])

class Form2(forms.Form):

    AGE_GROUP_CHOICES = [
    ("0-6 tháng", "0-6 tháng"),
    ("6-12 tháng", "6-12 tháng"),
    ("1-2 tuổi", "1-2 tuổi"),
    ("2-6 tuổi", "2-6 tuổi"),
    ("2-10 tuổi", "2-10 tuổi"),
    ("Trên 2 tuổi", "Trên 2 tuổi"),
    ("3-6 tuổi", "3-6 tuổi"),
    ("Trên 6 tuổi", "Trên 6 tuổi"),
    ("Mọi lứa tuổi", "Mọi lứa tuổi"),
    ("Người cao tuổi", "Người cao tuổi"),
    ("Trẻ biếng ăn", "Trẻ biếng ăn"),
    ("Trẻ suy dinh dưỡng", "Trẻ suy dinh dưỡng"),
    ]

    label = forms.ChoiceField(
        label="Chọn nhóm tuổi",
        choices=AGE_GROUP_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),  # Thêm class CSS nếu cần
    )


    natri = forms.FloatField(label="Natri (mg)", initial=0, 
        validators=[validate_positive])
    kali = forms.FloatField(label="Kali (mg)", initial=0, 
        validators=[validate_positive])
    clorid = forms.FloatField(label="Clorid (mg)", initial=0, 
        validators=[validate_positive])
    calci = forms.FloatField(label="Calci (mg)", initial=0, 
        validators=[validate_positive])
    phospho = forms.FloatField(label="Phospho (mg)", initial=0, 
        validators=[validate_positive])
    magnesi = forms.FloatField(label="Magnesi (mg)", initial=0, 
        validators=[validate_positive])
    mangan = forms.FloatField(label="Mangan (μg)", initial=0, 
        validators=[validate_positive])
    sat = forms.FloatField(label="Sắt (mg)", initial=0, 
        validators=[validate_positive])
    iot = forms.FloatField(label="I-ốt (μg)", initial=0, 
        validators=[validate_positive])
    kem = forms.FloatField(label="Kẽm (mg)", initial=0, 
        validators=[validate_positive])
    dong = forms.FloatField(label="Đồng (mg)", initial=0, 
        validators=[validate_positive])
    selen = forms.FloatField(label="Selen (μg)", initial=0, 
        validators=[validate_positive])
    vitamin_a = forms.FloatField(label="Vitamin A (IU)", initial=0, 
        validators=[validate_positive])
    vitamin_d3 = forms.FloatField(label="Vitamin D3 (IU)", initial=0, 
        validators=[validate_positive])
    vitamin_e = forms.FloatField(label="Vitamin E (mg α-TE)", initial=0, 
        validators=[validate_positive])
    vitamin_k1 = forms.FloatField(label="Vitamin K1 (μg)", initial=0, 
        validators=[validate_positive])
    vitamin_c = forms.FloatField(label="Vitamin C (mg)", initial=0, 
        validators=[validate_positive])
    vitamin_b1 = forms.FloatField(label="Vitamin B1 (mg)", initial=0, 
        validators=[validate_positive])
    vitamin_b2 = forms.FloatField(label="Vitamin B2 (mg)", initial=0, 
        validators=[validate_positive])
    niacin = forms.FloatField(label="Niacin (mg)", initial=0, 
        validators=[validate_positive])
    vitamin_b6 = forms.FloatField(label="Vitamin B6 (mg)", initial=0, 
        validators=[validate_positive])
    acid_folic = forms.FloatField(label="Acid folic (μg)", initial=0, 
        validators=[validate_positive])
    acid_pantothetic = forms.FloatField(label="Acid pantothetic (mg)", initial=0, 
        validators=[validate_positive])
    vitamin_b12 = forms.FloatField(label="Vitamin B12 (μg)", initial=0, 
        validators=[validate_positive])
    biotin = forms.FloatField(label="Biotin (μg)", initial=0, 
        validators=[validate_positive])
    cholin = forms.FloatField(label="Cholin (mg)", initial=0, 
        validators=[validate_positive])
    vitamin_k2 = forms.FloatField(label="Vitamin K2 (μg)", initial=0, 
        validators=[validate_positive])
    acid_linoleic = forms.FloatField(label="Acid linoleic (mg)", initial=0, 
        validators=[validate_positive])
    acid_alpha_linolenic = forms.FloatField(label="Acid alpha-linolenic (mg)", initial=0, 
        validators=[validate_positive])
    ara = forms.FloatField(label="ARA (Arachidonic acid) (mg)", initial=0, 
        validators=[validate_positive])
    dha = forms.FloatField(label="DHA (Docosahexaenoic acid) (mg)", initial=0, 
        validators=[validate_positive])
    acid_oleic = forms.FloatField(label="Acid Oleic (mg)", initial=0, 
        validators=[validate_positive])
    pufa = forms.FloatField(label="PUFA (g)", initial=0, 
        validators=[validate_positive])
    mufa = forms.FloatField(label="MUFA (g)", initial=0, 
        validators=[validate_positive])
    mct = forms.FloatField(label="MCT (g)", initial=0, 
        validators=[validate_positive])
    nang_luong = forms.FloatField(label="Năng lượng (kcal)", initial=0, 
        validators=[validate_positive])
    chat_dam = forms.FloatField(label="Chất đạm (g)", initial=0, 
        validators=[validate_positive])
    tryptophan = forms.FloatField(label="Tryptophan (mg)", initial=0, 
        validators=[validate_positive])
    chat_beo = forms.FloatField(label="Chất béo (g)", initial=0, 
        validators=[validate_positive])
    hydrat_cacbon = forms.FloatField(label="Hyđrat cacbon (g)", initial=0, 
        validators=[validate_positive])
    chat_xo_hoa_tan = forms.FloatField(label="Chất xơ hòa tan (g)", initial=0, 
        validators=[validate_positive])
    gos = forms.FloatField(label="GOS (g)", initial=0, 
        validators=[validate_positive])
    fl = forms.FloatField(label="2′-Fucosyllactose (2′-FL) (mg)", initial=0, 
        validators=[validate_positive])
    taurin = forms.FloatField(label="Taurin (mg)", initial=0, 
        validators=[validate_positive])
    inositol = forms.FloatField(label="Inositol (mg)", initial=0, 
        validators=[validate_positive])
    l_carnitin = forms.FloatField(label="L-Carnitin (mg)", initial=0, 
        validators=[validate_positive])
    nucleotid = forms.FloatField(label="Nucleotid (mg)", initial=0, 
        validators=[validate_positive])
    lutein = forms.FloatField(label="Lutein (μg)", initial=0, 
        validators=[validate_positive])
    do_am = forms.FloatField(label="Độ ẩm (g)", initial=0, 
        validators=[validate_positive])
    bifidobacterium = forms.FloatField(label="Bifidobacterium (cfu)", initial=0, 
        validators=[validate_positive])
    lactobacillus_rhamnosus = forms.FloatField(label="Lactobacillus rhamnosus (cfu)", initial=0, 
        validators=[validate_positive])
    lysin = forms.FloatField(label="Lysin (mg)", initial=0, 
        validators=[validate_positive])
    beta_caroten = forms.FloatField(label="Beta-caroten (μg)", initial=0, 
        validators=[validate_positive])
    collagen = forms.FloatField(label="Collagen (g)", initial=0, 
        validators=[validate_positive])
    molybden = forms.FloatField(label="Molybden (μg)", initial=0, 
        validators=[validate_positive])
    vitamin_pp = forms.FloatField(label="Vitamin PP (mg)", initial=0, 
        validators=[validate_positive])
    crom = forms.FloatField(label="Crôm (μg)", initial=0, 
        validators=[validate_positive])
    phosphatidylserine = forms.FloatField(label="Phosphatidylserine (mg)", initial=0, 
        validators=[validate_positive])
    vitamin_b9 = forms.FloatField(label="Vitamin B9 (mcg)", initial=0, 
        validators=[validate_positive])
    vitamin_b5 = forms.FloatField(label="Vitamin B5 (mg)", initial=0, 
        validators=[validate_positive])
    canxi = forms.FloatField(label="Canxi (mg)", initial=0, 
        validators=[validate_positive])
    cholesterol = forms.FloatField(label="Cholesterol (mg)", initial=0, 
        validators=[validate_positive])
    vitamin_b3 = forms.FloatField(label="Vitamin B3 (mg)", initial=0, 
        validators=[validate_positive])

class Form3(forms.Form):
    Loai_Men = forms.ChoiceField(
        label="Chọn loại men",
        choices=[("Streptococcus thermophilus và Lactobacillus bulgaricus","Streptococcus thermophilus và Lactobacillus bulgaricus"),],
        widget=forms.Select(attrs={"class": "form-control"}),  # Thêm class CSS nếu cần
    )
    Vi = forms.ChoiceField(
        label="Chọn vị",
        choices=[
                ("Ít đường","Ít đường"),
                ("Có đường","Có đường"),
                ("Không đường","Không đường"),
                ("Nha đam có đường","Nha đam có đường"),
                ("Trái cây","Trái cây"),
                ("Nha đam","Nha đam"),
                ("Lựu đỏ","Lựu đỏ"),
                ("Nếp ẩm","Nếp ẩm"),
                ("Trân châu đường đen","Trân châu đường đen"),
                ("Dâu","Dâu"),
                ("Việt quất","Việt quất"),
                ("Thạch dừa lá Dứa ít đường","Thạch dừa lá Dứa ít đường"),
                ],
        widget=forms.Select(attrs={"class": "form-control"}),  # Thêm class CSS nếu cần
    )

    Nang_luong = forms.FloatField(label="Năng lượng (kcal)", initial=0, 
        validators=[validate_positive])
    Hydrat_carbon = forms.FloatField(label="Hydrat carbon (g)", initial=0, 
        validators=[validate_positive])
    Chat_dam = forms.FloatField(label="Chất đạm (g)", initial=0, 
        validators=[validate_positive])
    Chat_beo = forms.FloatField(label="Chất béo (g)", initial=0, 
        validators=[validate_positive])
    Ti_le_sua_tuoi = forms.FloatField(label="Tỉ lệ sữa tươi", initial=0, 
        validators=[validate_positive])
    Ti_le_nha_dam = forms.FloatField(label="Tỉ lệ nha đam", initial=0, 
        validators=[validate_positive])
    Ti_le_mut_trai_cay = forms.FloatField(label="Tỉ lệ mứt trái cây", initial=0, 
        validators=[validate_positive])
    Collagen = forms.FloatField(label="Collagen (mg)", initial=0, 
        validators=[validate_positive])
    Ti_le_mut_luu = forms.FloatField(label="Tỉ lệ mứt lựu", initial=0, 
        validators=[validate_positive])
    Ti_le_thach_dua = forms.FloatField(label="Tỉ lệ thạch dừa", initial=0, 
        validators=[validate_positive])
    Ti_le_nep_cam = forms.FloatField(label="Tỉ lệ nếp cẩm", initial=0, 
        validators=[validate_positive])
    Ti_le_tran_chau_duong_den = forms.FloatField(label="Tỉ lệ trân châu đường đen", initial=0, 
        validators=[validate_positive])
    Ti_le_mut_dau = forms.FloatField(label="Tỉ lệ mứt dâu", initial=0, 
        validators=[validate_positive])
    Ti_le_mut_viet_quat = forms.FloatField(label="Tỉ lệ mứt việt quất", initial=0, 
        validators=[validate_positive])
    Ti_le_mut_la_dua = forms.FloatField(label="Tỉ lệ mứt lá dứa", initial=0, 
        validators=[validate_positive])
    Ti_le_sua_bot_tach_beo = forms.FloatField(label="Tỉ lệ sữa bột tách béo", initial=0, 
        validators=[validate_positive])
    Ti_le_sua_chua_len_men_tu_nhien = forms.FloatField(label="Tỉ lệ Sữa chua lên men tự nhiên", initial=0, 
        validators=[validate_positive])
    Calci = forms.FloatField(label="Calci (mg)", initial=0, 
        validators=[validate_positive])
    Natri = forms.FloatField(label="Natri (mg)", initial=0, 
        validators=[validate_positive])
    Lysin = forms.FloatField(label="Lysin (mg)", initial=0, 
        validators=[validate_positive])
    Kenm = forms.FloatField(label="Kẽm (mg)", initial=0, 
        validators=[validate_positive])
    Magie = forms.FloatField(label="Magie (mg)", initial=0, 
        validators=[validate_positive])
    Axit_Folic = forms.FloatField(label="Axit Folic (µg)", initial=0, 
        validators=[validate_positive])
    Vitamin_D3 = forms.FloatField(label="Vitamin D3 (IU)", initial=0, 
        validators=[validate_positive])
    Vitamin_A = forms.FloatField(label="Vitamin A (IU)", initial=0, 
        validators=[validate_positive])
    Vitamin_B1 = forms.FloatField(label="Vitamin B1 (µg)", initial=0, 
        validators=[validate_positive])
    Vitamin_B6 = forms.FloatField(label="Vitamin B6 (µg)", initial=0, 
        validators=[validate_positive])
    Vitamin_B9 = forms.FloatField(label="Vitamin B9 (µg)", initial=0, 
        validators=[validate_positive])
    Vitamin_B12 = forms.FloatField(label="Vitamin B12 (µg)", initial=0, 
        validators=[validate_positive])
    Vitamin_B3 = forms.FloatField(label="Vitamin B3 (µg)", initial=0, 
        validators=[validate_positive])
    Vitamin_B2 = forms.FloatField(label="Vitamin B2 (µg)", initial=0, 
        validators=[validate_positive])
    Ti_le_ngu_goc_cacao = forms.FloatField(label="Tỉ lệ ngũ gốc cacao làm form", initial=0, 
        validators=[validate_positive])

class Form4(forms.Form):
    Loai_Men = forms.ChoiceField(
        label="Chọn loại men",
        choices=[
            ("Streptococcus thermophilus và Lactobacillus bulgaricus", "Streptococcus thermophilus và Lactobacillus bulgaricus"),
            ("Lactobacillus paracasei","Lactobacillus paracasei")
        ],
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    # Các trường dinh dưỡng
    
    Hydrat_carbon = forms.FloatField(label="Hydrat carbon (g)", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Chat_dam = forms.FloatField(label="Chất đạm (g)", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Chat_beo = forms.FloatField(label="Chất béo (g)", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Ti_le_sua_tuoi = forms.FloatField(label="Tỉ lệ sữa tươi", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Ti_le_nha_dam = forms.FloatField(label="Tỉ lệ nha đam", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Ti_le_mut_trai_cay = forms.FloatField(label="Tỉ lệ mứt trái cây", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Collagen = forms.FloatField(label="Collagen (mg)", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Ti_le_mut_luu = forms.FloatField(label="Tỉ lệ mứt lựu", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Ti_le_thach_dua = forms.FloatField(label="Tỉ lệ thạch dừa", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Ti_le_nep_cam = forms.FloatField(label="Tỉ lệ nếp cẩm", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Ti_le_tran_chau_duong_den = forms.FloatField(label="Tỉ lệ trân châu đường đen", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Ti_le_mut_dau = forms.FloatField(label="Tỉ lệ mứt dâu", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Ti_le_mut_viet_quat = forms.FloatField(label="Tỉ lệ mứt việt quất", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Ti_le_mut_la_dua = forms.FloatField(label="Tỉ lệ mứt lá dứa", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Ti_le_sua_bot_tach_beo = forms.FloatField(label="Tỉ lệ sữa bột tách béo", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Ti_le_sua_chua_len_men_tu_nhien = forms.FloatField(label="Tỉ lệ Sữa chua lên men tự nhiên", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Calci = forms.FloatField(label="Calci (mg)", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Natri = forms.FloatField(label="Natri (mg)", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Lysin = forms.FloatField(label="Lysin (mg)", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Kenm = forms.FloatField(label="Kẽm (mg)", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Magie = forms.FloatField(label="Magie (mg)", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Axit_Folic = forms.FloatField(label="Axit Folic (µg)", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Vitamin_D3 = forms.FloatField(label="Vitamin D3 (IU)", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Vitamin_A = forms.FloatField(label="Vitamin A (IU)", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Vitamin_B1 = forms.FloatField(label="Vitamin B1 (µg)", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Vitamin_B6 = forms.FloatField(label="Vitamin B6 (µg)", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Vitamin_B9 = forms.FloatField(label="Vitamin B9 (µg)", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Vitamin_B12 = forms.FloatField(label="Vitamin B12 (µg)", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Vitamin_B3 = forms.FloatField(label="Vitamin B3 (µg)", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Vitamin_B2 = forms.FloatField(label="Vitamin B2 (µg)", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))
    Ti_le_ngu_goc_cacao = forms.FloatField(label="Tỉ lệ ngũ gốc cacao", initial=0, 
        validators=[validate_positive], widget=forms.NumberInput(attrs={"class": "form-control"}))

class Form5(forms.Form):
    Flavor = forms.ChoiceField(
        label="Flavor",
        choices=[
                ("Vị có đường", "Vị có đường"),
                ("Vị ít đường", "Vị ít đường"),
                ("Vị ít đường", "Vị ít đường"),
                ("Vị organic", "Vị organic"),
                ("Vị không đường", "Vị không đường"),
                ("Vị ít đường", "Vị ít đường"),
                ("Vị có đường", "Vị có đường"),
                ("Vị không đường", "Vị không đường"),
                ("Vị socola", "Vị socola"),
                ("Vị ít đường", "Vị ít đường"),
                ("Vị dâu", "Vị dâu"),
                ("Tách béo", "Tách béo"),
                ("Vị dừa", "Vị dừa"),
                ("Vị chuối", "Vị chuối"),
                ("Nguyên bản", "Nguyên bản"),
                ("Vị ít đường", "Vị ít đường"),
                ("Vị có đường", "Vị có đường"),
                ("organic", "organic"),
                ("Nguyên bản", "Nguyên bản"),
                ("Vị dâu", "Vị dâu"),
                ("Vị socola", "Vị socola")
                ],
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    Energy = forms.FloatField(
        label="Energy (kcal)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Fat = forms.FloatField(
        label="Fat (g)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Protein = forms.FloatField(
        label="Protein (g)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Carbohydrate = forms.FloatField(
        label="Carbohydrate (g)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Calcium = forms.FloatField(
        label="Calcium (mg)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Zinc = forms.FloatField(
        label="Zinc (mcg)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Phosporus = forms.FloatField(
        label="Phosporus (mg)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Selenium = forms.FloatField(
        label="Selenium (mcg)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Magnesi = forms.FloatField(
        label="Magnesi (mg)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Vitamin_A = forms.FloatField(
        label="Vitamin A (IU)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Vitamin_D3 = forms.FloatField(
        label="Vitamin D3 (IU)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Vitamin_B2 = forms.FloatField(
        label="Vitamin B2 (mcg)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Natri = forms.FloatField(
        label="Natri (mg)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Vitamin_B12 = forms.FloatField(
        label="Vitamin B12 (mcg)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Vitamin_D = forms.FloatField(
        label="Vitamin D (IU)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Vitamin_B1 = forms.FloatField(
        label="Vitamin B1 (mcg)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Fresh_Milk_Rate = forms.FloatField(
        label="Fresh Milk Rate", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Xenlulose = forms.FloatField(
        label="Xenlulose (g)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Vitamin_K2 = forms.FloatField(
        label="Vitamin K2 (mcg)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Vitamin_C = forms.FloatField(
        label="Vitamin C (mcg)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    GABA = forms.FloatField(
        label="GABA (mcg)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Vitamin_K1 = forms.FloatField(
        label="Vitamin K1 (mcg)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Axit_Pantothenic = forms.FloatField(
        label="Axit Pantothenic (mcg)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Axit_Folic = forms.FloatField(
        label="Axit Folic (mcg)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Biotin = forms.FloatField(
        label="Biotin (mcg)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Vitamin_PP = forms.FloatField(
        label="Vitamin PP (mcg)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    DHA = forms.FloatField(
        label="DHA (mg)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Vitamin_B6 = forms.FloatField(
        label="Vitamin B6 (mcg)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Iron = forms.FloatField(
        label="Iron (mg)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Potassium = forms.FloatField(
        label="Potassium (mg)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Vitamin_B3 = forms.FloatField(
        label="Vitamin B3 (mcg)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Iot = forms.FloatField(
        label="Iot (mcg)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    Lysin = forms.FloatField(
        label="Lysin (mg)", 
        initial=0, 
        validators=[validate_positive], 
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

