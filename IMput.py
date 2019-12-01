import cx_Oracle

conn = cx_Oracle.connect('VDMSTGADM/v2*L-6^Et-M_4d@dataservices3.imanheim.com/DENVO_OLTP1')
cur = conn.cursor()
cur.execute('Select * from ALTERYXOPTIONS fetch first 1 rows only')
for line in cur:
    print(line)
cur.close
conn.close