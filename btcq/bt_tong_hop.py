import re

def print_lines_with_condition(filename):

    try:
      with open(filename, 'r') as file:
            for line in file:
                # Loại bỏ khoảng trắng và xem xét các dòng thỏa điều kiện
                cl = line.strip()

               ####  Các dòng bắt đầu là 't' hoặc 'c', và chứa 're'
               # if (cl.startswith('t') or cl.startswith('c')) and 're' in cl:
                    #print(cl)

                #### Các dòng có ít nhất 25 ký tự
                # if len(cl) >= 25 :
                    #print(cl)

                ####Các dòng kết thúc bằng ký tự '?' hoặc '!'
                #if cl.endswith('?') or cl.endswith('!'):
                    #print(cl)

               #### Các dòng có chứa 'regular'
                #if 'regular' in cl.lower(): # chuyển đổi về chữ thường hàm lower(), và kiểm tra điều kiện có từ regular
                    #print(cl)

                ###in ra Các dòng chứa những ký tự: a, r, s, m, l (không cần liên tục)
                #if re.search('[arsml]', line):
                    #print(cl)

                ### Tìm kiếm các dòng không chứa ',' và '.'
                #if not re.search('[,.]', line):
                    #print(cl)

                ### Tìm kiếm các từ có số lượng ký tự 'a' bất kỳ và theo sau bởi 'b'
                #words = re.findall(r'\b\w*a\w*b\w*\b', line)
                #for word in words:
                    #print(word)

                #### Tìm kiếm các từ bắt đầu bằng số từ '0-9'
                #words = re.findall(r'\b\d\w*\b', line)
                #for word in words:
                    #print(word)

                ### Tìm kiếm các từ có chứa ký tự thường 'a-z' và số từ '0-9'
                #words = re.findall(r'\b[a-z0-9]+\b', line)

                #words = re.findall(r'\b[a-z_]+\b', line)
                #for word in words:
                    #print(word)


                #### Thay thế dấu '_' bằng khoảng trắng trong từng dòng
                #modified_line = re.sub(r'_', ' ', line)
                #print(modified_line)

                ### Tìm kiếm định dạng mm-dd-yy và thay thế bằng dd-mm-yy
                modified_line = re.sub(r'(\d{2})-(\d{2})-(\d{2})', r'\2-\1-\3', line)
                print(modified_line)

                 #### Tìm các địa chỉ email trong dòng
                #email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', line)
                #### Trích xuất và in ra domain từ địa chỉ email
                #for email in email_addresses:
                    #domain = email.split('@')[1]
                    #print(domain)


    except FileNotFoundError:
        print("Không tìm thấy tập tin.")

# Thay 'B1.txt' bằng tên tập tin văn bản của bạn
print_lines_with_condition('B1.txt')
