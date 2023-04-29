"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
"""


def ekstraksi_data():
    """
    Tanggal: 29 April 2023
    Waktu: 19:40:06 WIB
    Magnitudo: 2.8
    Kedalaman: 3 km
    Lokasi: LS=2.92 BT=119.40
    Pusat Gempa: Pusat gempa berada di darat 8 km Tenggara Mamasa
    Dirasakan: Dirasakan (Skala MMI): II Mamasa
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '29 April 2023'
    hasil['waktu'] = '19:40:06 WIB'
    hasil['magnitudo'] = 2.8
    hasil['kedalaman'] = '3 km'
    hasil['lokasi'] = {'ls':2.92, 'bt':119.40}
    hasil['pusat'] = 'Pusat gempa berada di darat 8 km Tenggara Mamasa'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II Mamasa'
    return hasil


def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Lokasi: LS={result['lokasi']['ls']} BT={result['lokasi']['bt']}")
    print(f"Pusat Gempa: {result['pusat']}")
    print(f"Dirasakan: {result['dirasakan']}")


if __name__ == '__main__':
    print('aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)
