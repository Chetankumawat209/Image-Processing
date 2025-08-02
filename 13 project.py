import cv2

def image_save(img):
        path = input("Enter the full path where you want to save the image (e.g., C:/Users/Name/Pictures/image.jpg)")
        cv2.imwrite(path, img)
        print(f'Your image save at {path} success fully')

def image_show(img):
        cv2.imshow('image', img)
        cv2.waitKey(10000)
        cv2.destroyAllWindows()

def draw_line(img):
    print('Enter starting coordinate (ex:-(x,y)')
    start_axis_x = int(input('Enter x '))
    start_axis_y = int(input('Enter y '))

    print('Enter ending coordinate (ex:-(x,y)')
    end_axis_x = int(input('Enter x '))
    end_axis_y = int(input('Enter y '))

    print('Enter color coding')
    B, G, R = map(int, input('Enter (b,g,r) separated by commas').split(','))
    thickness = int(input('Enter line thickness'))

    cv2.line(img, (start_axis_x, start_axis_y), (end_axis_x, end_axis_y), (B, G, R), thickness)
    print("What you want to save or show ")
    ss = int(input('press 1 for save or press 2 for show\n'))
    if ss == 1:
        image_save(img)
    elif ss == 2:
        image_show(img)
    else:
        raise ValueError('you enter wrong input')

def draw_rectange(img):
    print('Enter top coordinates (ex:-(x,y)')
    start_axis_x = int(input('Enter x '))
    start_axis_y = int(input('Enter y '))

    print('Enter bottom coordinate (ex:-(x,y)')
    end_axis_x = int(input('Enter x '))
    end_axis_y = int(input('Enter y '))

    print('Enter color coding ')
    B, G, R = map(int, input('Enter (b,g,r) separated by commas').split(','))

    thickness = int(input('Enter line thickness '))

    cv2.rectangle(img, (start_axis_x, start_axis_y), (end_axis_x, end_axis_y), (B, G, R), thickness)
    print("What you want to save or show ")
    ss = int(input('press 1 for save or press 2 for show\n'))
    if ss == 1:
        image_save(img)
    elif ss == 2:
        image_show(img)
    else:
        raise ValueError('you enter wrong input')


def draw_circle(img):
    print('Enter center coordinates (ex:-(x,y)')
    center_x = int(input('Enter x '))
    center_y = int(input('Enter y '))

    radius=int(input('Enter radius of circle '))

    print('Enter color coding ')
    B, G, R = map(int, input('Enter (b,g,r) separated by commas').split(','))

    thickness = int(input('Enter line thickness '))

    cv2.circle(img, (center_x,center_y),radius,(B, G, R), thickness)
    print("What you want to save or show ")
    ss = int(input('press 1 for save or press 2 for show\n'))
    if ss == 1:
        image_save(img)
    elif ss == 2:
        image_show(img)
    else:
        raise ValueError('you enter wrong input')

def write_text(img):
    write=input('Enter the text ')
    print('Enter place coordinates (ex:-(x,y)')
    org_x = int(input('Enter x '))
    org_y = int(input('Enter y '))

    font=cv2.FONT_HERSHEY_PLAIN
    fontScale=4

    print('Enter color coding ')
    B, G, R = map(int, input('Enter (b,g,r) separated by commas').split(','))

    thickness = int(input('Enter line thickness '))

    cv2.putText(img, write,(org_x,org_y),font,fontScale,(B, G, R), thickness)
    print("What you want to save or show ")
    ss = int(input('press 1 for save or press 2 for show\n'))
    if ss == 1:
        image_save(img)
    elif ss == 2:
        image_show(img)
    else:
        raise ValueError('you enter wrong input')


def main():
    file_location = input('Enter your image location with name ')
    img = cv2.imread(file_location)

    try:

        if img is not None:

            inputs = input('What you want to draw (line ,circle,rectangle,text) ')

            if (inputs =='LINE' ) or (inputs == 'line'):
                draw_line(img)

            elif (inputs =='CIRCLE' ) or (inputs == 'circle'):
                draw_circle(img)

            elif (inputs =='RECTANGLE' ) or (inputs == 'rectangle'):
                draw_rectange(img)

            elif (inputs =='TEXT' ) or (inputs == 'text'):
                write_text(img)
            else:
                print('input must be capitalize or upper case')


        else:
            raise FileNotFoundError ('file not found path of image')
    except ValueError:
        print("Inputs issue")

if __name__=="__main__":
    main()