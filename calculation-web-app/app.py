from flask import Flask, request, render_template_string
import math
from collections import Counter
from sympy import symbols, limit as sym_limit, diff, sympify

app = Flask(__name__)

# =========================
# HALAMAN UTAMA
# =========================
@app.route("/")
def main_menu():
    return render_template_string("""
        <h1>RUMUS RUMUSS</h1>
        <ul>
            <li><a href='/bangun_datar'>Bangun Datar</a></li>
            <li><a href='/bangun_ruang'>Bangun Ruang</a></li>
            <li><a href='/fungsi'>Fungsi Matematika</a></li>
            <li><a href='/suhu'>Konversi Suhu</a></li>
            <li><a href='/logaritma'>Logaritma</a></li>
            <li><a href='/integral'>Integral</a></li>
            <li><a href='/persamaan'>Persamaan</a></li>
            <li><a href='/statistika'>Statistika</a></li>
            <li><a href='/limit'>Limit</a></li>
            <li><a href='/turunan'>Turunan/Derivatif</a></li>
        </ul>
    """)

# =========================
# BANGUN DATAR
# =========================
@app.route("/bangun_datar", methods=["GET", "POST"])
def bangun_datar():
    if request.method == "POST":
        pilih = request.form.get("pilih")
        if pilih == "1":
            sisi = float(request.form.get("sisi"))
            luas = sisi * sisi
            keliling = 4 * sisi
            return f"Luas Persegi = {luas}, Keliling = {keliling}<br><a href='/bangun_datar'>Kembali</a>"
        elif pilih == "2":
            p = float(request.form.get("p"))
            l = float(request.form.get("l"))
            luas = p*l
            keliling = 2*(p+l)
            return f"Luas Persegi Panjang = {luas}, Keliling = {keliling}<br><a href='/bangun_datar'>Kembali</a>"
        # Tambahkan semua bangun datar lain di sini
    return render_template_string("""
        <h2>Bangun Datar</h2>
        <form method='post'>
            <label>Pilih Bangun:</label>
            <select name='pilih'>
                <option value='1'>Persegi</option>
                <option value='2'>Persegi Panjang</option>
                <option value='3'>Segitiga</option>
                <option value='4'>Lingkaran</option>
                <option value='5'>Trapesium</option>
                <option value='6'>Jajar Genjang</option>
                <option value='7'>Belah Ketupat</option>
                <option value='8'>Layang-layang</option>
                <option value='9'>Poligon</option>
                <option value='10'>Segi Lima</option>
                <option value='11'>Segi Enam</option>
            </select><br>
            <label>Input parameter sesuai pilihan di atas:</label><br>
            <input type='text' name='sisi' placeholder='sisi'>
            <input type='text' name='p' placeholder='panjang'>
            <input type='text' name='l' placeholder='lebar'>
            <button type='submit'>Hitung</button>
        </form>
        <a href='/'>Kembali ke Menu Utama</a>
    """)

# =========================
# BANGUN RUANG
# =========================
@app.route("/bangun_ruang", methods=["GET", "POST"])
def bangun_ruang():
    if request.method == "POST":
        pilih = request.form.get("pilih")
        if pilih == "1":
            sisi = float(request.form.get("sisi"))
            volume = sisi ** 3
            luas_permukaan = 6 * sisi * sisi
            return f"Volume Kubus = {volume}, Luas Permukaan = {luas_permukaan}<br><a href='/bangun_ruang'>Kembali</a>"
        elif pilih == "2":
            p = float(request.form.get("p"))
            l = float(request.form.get("l"))
            t = float(request.form.get("t"))
            volume = p*l*t
            luas_permukaan = 2*(p*l + p*t + l*t)
            return f"Volume Balok = {volume}, Luas Permukaan = {luas_permukaan}<br><a href='/bangun_ruang'>Kembali</a>"
        # Tambahkan bangun ruang lainnya
    return render_template_string("""
        <h2>Bangun Ruang</h2>
        <form method='post'>
            <label>Pilih Bangun:</label>
            <select name='pilih'>
                <option value='1'>Kubus</option>
                <option value='2'>Balok</option>
                <option value='3'>Bola</option>
                <option value='4'>Silinder</option>
                <option value='5'>Kerucut</option>
            </select><br>
            <input type='text' name='sisi' placeholder='sisi'>
            <input type='text' name='p' placeholder='panjang'>
            <input type='text' name='l' placeholder='lebar'>
            <input type='text' name='t' placeholder='tinggi'>
            <input type='text' name='r' placeholder='jari-jari'>
            <button type='submit'>Hitung</button>
        </form>
        <a href='/'>Kembali ke Menu Utama</a>
    """)

# =========================
# FUNGSI MATEMATIKA
# =========================
@app.route("/fungsi", methods=["GET", "POST"])
def fungsi():
    if request.method == "POST":
        pilih = request.form.get("pilih")
        if pilih == "1":
            a = float(request.form.get("a"))
            b = float(request.form.get("b"))
            c = float(request.form.get("c"))
            d = b**2 - 4*a*c
            if d < 0:
                return "Tidak ada akar real<br><a href='/fungsi'>Kembali</a>"
            x1 = (-b + math.sqrt(d))/(2*a)
            x2 = (-b - math.sqrt(d))/(2*a)
            return f"Akar kuadrat: {x1}, {x2}<br><a href='/fungsi'>Kembali</a>"
        elif pilih == "2":
            m = float(request.form.get("m"))
            b = float(request.form.get("b"))
            x = float(request.form.get("x"))
            y = m*x+b
            return f"Nilai y = {y}<br><a href='/fungsi'>Kembali</a>"
        elif pilih == "3":
            a = float(request.form.get("a"))
            x = float(request.form.get("x"))
            y = a**x
            return f"Nilai y = {y}<br><a href='/fungsi'>Kembali</a>"
        elif pilih == "4":
            a = float(request.form.get("a"))
            y = float(request.form.get("y"))
            x = math.log(y, a)
            return f"Nilai x = {x}<br><a href='/fungsi'>Kembali</a>"
    return render_template_string("""
        <h2>Fungsi Matematika</h2>
        <form method='post'>
            <select name='pilih'>
                <option value='1'>Kuadrat</option>
                <option value='2'>Linier</option>
                <option value='3'>Eksponen</option>
                <option value='4'>Logaritma</option>
            </select><br>
            <input type='text' name='a' placeholder='a'>
            <input type='text' name='b' placeholder='b'>
            <input type='text' name='c' placeholder='c'>
            <input type='text' name='x' placeholder='x'>
            <input type='text' name='y' placeholder='y'>
            <button type='submit'>Hitung</button>
        </form>
        <a href='/'>Kembali</a>
    """)

# =========================
# Konversi Suhu
# =========================
@app.route("/suhu", methods=["GET", "POST"])
def suhu():
    if request.method == "POST":
        pilih = request.form.get("pilih")
        if pilih == "1":
            c = float(request.form.get("c"))
            f = (c*9/5)+32
            return f"{c} C = {f} F<br><a href='/suhu'>Kembali</a>"
        elif pilih == "2":
            f = float(request.form.get("f"))
            c = (f-32)*5/9
            return f"{f} F = {c} C<br><a href='/suhu'>Kembali</a>"
        # Tambahkan semua opsi suhu lain
    return render_template_string("""
        <h2>Konversi Suhu</h2>
        <form method='post'>
            <select name='pilih'>
                <option value='1'>Celsius ke Fahrenheit</option>
                <option value='2'>Fahrenheit ke Celsius</option>
            </select><br>
            <input type='text' name='c' placeholder='Celsius'>
            <input type='text' name='f' placeholder='Fahrenheit'>
            <button type='submit'>Konversi</button>
        </form>
        <a href='/'>Kembali</a>
    """)

# =========================
# LOGARITMA
# =========================
@app.route("/logaritma", methods=["GET", "POST"])
def logaritma():
    if request.method == "POST":
        pilih = request.form.get("pilih")
        x = float(request.form.get("x"))
        if pilih == "1":
            return f"log10({x}) = {math.log10(x)}<br><a href='/logaritma'>Kembali</a>"
        elif pilih == "2":
            return f"ln({x}) = {math.log(x)}<br><a href='/logaritma'>Kembali</a>"
        elif pilih == "3":
            b = float(request.form.get("b"))
            return f"log base {b} dari {x} = {math.log(x,b)}<br><a href='/logaritma'>Kembali</a>"
    return render_template_string("""
        <h2>Logaritma</h2>
        <form method='post'>
            <select name='pilih'>
                <option value='1'>Basis 10</option>
                <option value='2'>Basis e</option>
                <option value='3'>Basis b</option>
            </select><br>
            <input type='text' name='x' placeholder='x'>
            <input type='text' name='b' placeholder='basis'>
            <button type='submit'>Hitung</button>
        </form>
        <a href='/'>Kembali</a>
    """)

# =========================
# INTEGRAL
# =========================
@app.route("/integral", methods=["GET", "POST"])
def integral():
    if request.method == "POST":
        pilih = request.form.get("pilih")
        a = float(request.form.get("a"))
        n = float(request.form.get("n"))
        if pilih == "1":
            return f"Integral tak tentu = ({a}/{n+1})x^{n+1} + C<br><a href='/integral'>Kembali</a>"
        elif pilih == "2":
            x1 = float(request.form.get("x1"))
            x2 = float(request.form.get("x2"))
            integral_a = (a/(n+1))*(x1**(n+1))
            integral_b = (a/(n+1))*(x2**(n+1))
            hasil = integral_b - integral_a
            return f"Integral tentu = {hasil}<br><a href='/integral'>Kembali</a>"
    return render_template_string("""
        <h2>Integral</h2>
        <form method='post'>
            <select name='pilih'>
                <option value='1'>Tak Tentu</option>
                <option value='2'>Tentu</option>
            </select><br>
            <input type='text' name='a' placeholder='koefisien'>
            <input type='text' name='n' placeholder='pangkat'>
            <input type='text' name='x1' placeholder='batas bawah'>
            <input type='text' name='x2' placeholder='batas atas'>
            <button type='submit'>Hitung</button>
        </form>
        <a href='/'>Kembali</a>
    """)

# =========================
# PERSAMAAN
# =========================
@app.route("/persamaan", methods=["GET", "POST"])
def persamaan():
    if request.method == "POST":
        pilih = request.form.get("pilih")
        if pilih == "1":
            m = float(request.form.get("m"))
            b = float(request.form.get("b"))
            x = float(request.form.get("x"))
            y = m*x+b
            return f"y = {y}<br><a href='/persamaan'>Kembali</a>"
        elif pilih == "2":
            a = float(request.form.get("a"))
            b = float(request.form.get("b"))
            c = float(request.form.get("c"))
            d = b**2 - 4*a*c
            if d < 0:
                return "Tidak ada akar real<br><a href='/persamaan'>Kembali</a>"
            x1 = (-b+math.sqrt(d))/(2*a)
            x2 = (-b-math.sqrt(d))/(2*a)
            return f"Akar: {x1}, {x2}<br><a href='/persamaan'>Kembali</a>"
    return render_template_string("""
        <h2>Persamaan</h2>
        <form method='post'>
            <select name='pilih'>
                <option value='1'>Linier</option>
                <option value='2'>Kuadrat</option>
            </select><br>
            <input type='text' name='a' placeholder='a'>
            <input type='text' name='b' placeholder='b'>
            <input type='text' name='c' placeholder='c'>
            <input type='text' name='m' placeholder='m'>
            <input type='text' name='x' placeholder='x'>
            <button type='submit'>Hitung</button>
        </form>
        <a href='/'>Kembali</a>
    """)

# =========================
# STATISTIKA
# =========================
@app.route("/statistika", methods=["GET", "POST"])
def statistika():
    if request.method == "POST":
        data = request.form.get("data")
        pilih = request.form.get("pilih")
        data_list = list(map(float, data.split()))
        n = len(data_list)
        if pilih == "1":
            mean = sum(data_list) / n
            return f"Mean: {mean}<br><a href='/statistika'>Kembali</a>"
        elif pilih == "2":
            data_list.sort()
            if n % 2 == 0:
                median = (data_list[n//2 - 1] + data_list[n//2]) / 2
            else:
                median = data_list[n//2]
            return f"Median: {median}<br><a href='/statistika'>Kembali</a>"
        elif pilih == "3":
            modus = Counter(data_list).most_common(1)[0][0]
            return f"Modus: {modus}<br><a href='/statistika'>Kembali</a>"
        elif pilih == "4":
            mean = sum(data_list) / n
            varians = sum((x - mean) ** 2 for x in data_list) / n
            return f"Varians: {varians}<br><a href='/statistika'>Kembali</a>"
        elif pilih == "5":
            mean = sum(data_list) / n
            varians = sum((x - mean) ** 2 for x in data_list) / n
            std_dev = varians ** 0.5
            return f"Standar Deviasi: {std_dev}<br><a href='/statistika'>Kembali</a>"
    return render_template_string("""
        <h2>Statistika</h2>
        <form method='post'>
            <input type='text' name='data' placeholder='Masukkan data pisahkan dengan spasi'>
            <select name='pilih'>
                <option value='1'>Mean</option>
                <option value='2'>Median</option>
                <option value='3'>Modus</option>
                <option value='4'>Varians</option>
                <option value='5'>Standar Deviasi</option>
            </select>
            <button type='submit'>Hitung</button>
        </form>
        <a href='/'>Kembali</a>
    """)


@app.route("/limit", methods=["GET", "POST"])
def limit():
    if request.method == "POST":
        f = request.form.get("f")
        x0 = float(request.form.get("x0"))
        x = symbols('x')
        try:
            hasil = sym_limit(sympify(f), x, x0)
            return f"Limit f(x) saat x->{x0} = {hasil}<br><a href='/limit'>Kembali</a>"
        except Exception as e:
            return f"Error: {e}<br><a href='/limit'>Kembali</a>"
    return render_template_string("""
        <h2>Limit</h2>
        <form method='post'>
            <input type='text' name='f' placeholder='Masukkan fungsi f(x)'>
            <input type='text' name='x0' placeholder='x ->'>
            <button type='submit'>Hitung</button>
        </form>
        <a href='/'>Kembali</a>
    """)


@app.route("/derivatif", methods=["GET", "POST"])
def derivatif():
    if request.method == "POST":
        f = request.form.get("f")
        x = symbols('x')
        try:
            hasil = diff(sympify(f), x)
            return f"Derivatif dari {f} = {hasil}<br><a href='/derivatif'>Kembali</a>"
        except Exception as e:
            return f"Error: {e}<br><a href='/derivatif'>Kembali</a>"
    return render_template_string("""
        <h2>Derivatif</h2>
        <form method='post'>
            <input type='text' name='f' placeholder='Masukkan fungsi f(x)'>
            <button type='submit'>Hitung</button>
        </form>
        <a href='/'>Kembali</a>
    """)


@app.route("/turunan", methods=["GET", "POST"])
def turunan():
    if request.method == "POST":
        f = request.form.get("f")
        x = symbols('x')
        try:
            hasil = diff(sympify(f), x)
            return f"Turunan dari {f} = {hasil}<br><a href='/turunan'>Kembali</a>"
        except Exception as e:
            return f"Error: {e}<br><a href='/turunan'>Kembali</a>"
    return render_template_string("""
        <h2>Turunan</h2>
        <form method='post'>
            <input type='text' name='f' placeholder='Masukkan fungsi f(x)'>
            <button type='submit'>Hitung</button>
        </form>
        <a href='/'>Kembali</a>
    """)


if __name__ == "__main__":
    app.run(debug=True)