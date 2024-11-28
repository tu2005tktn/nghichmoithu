import os
import cv2

def pencil_sketch(image_path, output_path):
    # Lấy đường dẫn thư mục từ output_path
    output_dir = os.path.dirname(output_path)

    # Kiểm tra xem thư mục output có tồn tại không, nếu không thì tạo mới
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Thư mục '{output_dir}' đã được tạo.")

    # Đọc ảnh từ đường dẫn
    image = cv2.imread(image_path)
    if image is None:
        print(f"Không thể đọc ảnh từ {image_path}")
        return
    
    # Tiến hành các bước xử lý ảnh
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_gray_image = cv2.bitwise_not(gray_image)
    blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
    inverted_blurred_image = cv2.bitwise_not(blurred_image)
    pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)
    
    # Lưu ảnh phác thảo vào file output
    cv2.imwrite(output_path, pencil_sketch_image)
    print(f"Đã lưu ảnh phác thảo tại {output_path}")
    
    # Hiển thị ảnh phác thảo
    cv2.imshow("Pencil Sketch", pencil_sketch_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Đặt đường dẫn đầu vào và đầu ra
input_image_path = 'w2.jpg'  # Đảm bảo file này tồn tại
output_image_path = 'output_images/w2_sketch.jpg'  # Nếu thư mục chưa có, chương trình sẽ tạo thư mục này

# Gọi hàm để tạo ảnh phác thảo
pencil_sketch(input_image_path, output_image_path)
