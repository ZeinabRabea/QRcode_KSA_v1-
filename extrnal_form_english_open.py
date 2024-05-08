
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from datetime import datetime
import qrcode
import base64
from datetime import datetime

def DecimalNumAscii(number):
    character = chr(number)
    return character



def select_image():
    global image_path

    image_path = filedialog.asksaveasfilename(defaultextension=".png",
                                               filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"),
                                                          ("All files", "*.*")])

    # استخدام متغيرات عالمية لتخزين القيم المدخلة
    global x1, x2, x3, x4, x5
    # حفظ القيم المدخلة في المتغيرات

    taxNumber = entry2.get()

    D = day_combobox.get()
    M = mon_combobox.current() + 1
    Y = year_combobox.get()
    Time = entry3T.get()
    T = Time.split(":")

    entered_time = datetime(int(Y), int(M), int(D), int(T[0]), int(T[1]), int(T[2]), 0)
    dateTime = entered_time.strftime("%Y-%m-%d %H:%M:%S")

    sellerName = entry1.get()
    invoiceAmount = entry4.get()
    vat = entry5.get()

    
    zz = len(str((sellerName))) 

    V1 = DecimalNumAscii(zz)
    
    V2 = DecimalNumAscii(15)
    V3 = DecimalNumAscii(len(str((dateTime))))
    V4 = DecimalNumAscii(len(str((invoiceAmount))))
    V5 = DecimalNumAscii(len(str((vat))))

    encoded_data = (
                "" + V1  + sellerName + "" + V2 + taxNumber + "" + V3 + dateTime + "" + V4 + invoiceAmount + "" + V5 + vat)

    # تشفير البيانات بواسطة Base64
    base64_encoded_data = base64.b64encode(encoded_data.encode('utf-8')).decode('utf-8')

    # إنشاء رمز الاستجابة السريعة
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(base64_encoded_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # حفظ الصورة إلى ملف
    x = image_path
    if x == '':
        x = "_" + Y + "_" + mon_combobox.get() + "_" + D + "_" + T[0] + "_" + T[1] + "_" + T[2] + ".Png"

    img.save(x)


    entry3T.delete(0, tk.END)  # مسح النص الحالي في مربع النص
    entry3T.insert(0, '')

    entry4.delete(0, tk.END)  # مسح النص الحالي في مربع النص
    entry4.insert(0, '')

    entry5.delete(0, tk.END)  # مسح النص الحالي في مربع النص
    entry5.insert(0, '')

    insert_time()


# إنشاء نافذة
root = tk.Tk()
root.title("Z_Rabea QRcode ")
root.geometry("600x400")  # تعيين حجم النافذة

# إنشاء وضبط عناصر واجهة المستخدم
labels = []
entries = []

# إنشاء وصف وعنصر إدخال البيانات للسطر الأول
label1 = tk.Label(root, text="اسم البائع:", width=20)
label1.grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root, width=50)
entry1.grid(row=0, column=1, padx=10, pady=5)
entry1.insert(0, "COMPANY NAME")
#entry1.config(state='readonly')

# إنشاء وصف وعنصر إدخال البيانات للسطر الثاني
label2 = tk.Label(root, text="الرقم الضريبي:", width=20)
label2.grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root, width=50)
entry2.grid(row=1, column=1, padx=10, pady=5)
entry2.insert(0, "311222244455553")
#entry2.config(state='readonly')

# إنشاء وصف وعنصر إدخال البيانات للسطر الثالث
label3 = tk.Label(root, text=" تاريخ الفاتورة:", width=20)
label3.grid(row=2, column=0, padx=10, pady=5)


days = [str(i).zfill(2) for i in range(1, 32)]
day_combobox = ttk.Combobox(root, values=days, width=10)
day_combobox.grid(row=2, column=1, padx=10, pady=5,sticky='w')

months = ["يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو", "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"]
mon_combobox = ttk.Combobox(root, values=months, width=10)
mon_combobox.grid(row=2, column=1, padx=10, pady=5,sticky='n')

years = list(range(2019, 2100))
year_combobox = ttk.Combobox(root, values=years, width=10)
year_combobox.grid(row=2, column=1, padx=10, pady=5,sticky='e')


label3 = tk.Label(root, text=" وقت الفاتورة:", width=20)
label3.grid(row=3, column=0, padx=10, pady=5)

entry3T = tk.Entry(root, width=20)
entry3T.grid(row=3, column=1, padx=5, pady=5, sticky='w')

def insert_time():
    dateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dateTime = dateTime.split()
    datee = dateTime[0].split("-")
    entry3T.insert(0, dateTime[1])

    day_combobox.current(int(datee[2]) - 1)  # تعيين القيمة المبدئية إلى القيمة ذات الفهرس 7 (الفهرس يبدأ من 0)
    mon_combobox.current(int(datee[1]) - 1)
    year_combobox.current(int(datee[0]) - 2019)


insert_time()



# إنشاء وصف وعنصر إدخال البيانات للسطر الرابع
label4 = tk.Label(root, text="مبلغ الفاتورة (مع القيمة المضافة):", width=25)
label4.grid(row=4, column=0, padx=10, pady=5)
entry4 = tk.Entry(root, width=50)
entry4.grid(row=4, column=1, padx=10, pady=5)

# إنشاء وصف وعنصر إدخال البيانات للسطر الخامس
label5 = tk.Label(root, text="ضريبة القيمة المضافة:", width=20)
label5.grid(row=5, column=0, padx=10, pady=5)
entry5 = tk.Entry(root, width=50)
entry5.grid(row=5, column=1, padx=10, pady=5)

# إنشاء عنصر اختيار لأيام الأسبوع





# إنشاء زر لاختيار الصورة
image_button = tk.Button(root, text="اختر مكان حفظ الصورة", command=select_image)
image_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)




# تعريف المسار الافتراضي للصورة كفارغ لتخزين مسار الصورة المحددة
image_path = ""

# تشغيل الحلقة الرئيسية
root.mainloop()
