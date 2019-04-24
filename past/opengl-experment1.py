from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def display():

    # /* 清除颜色缓存 */
    glClear (GL_COLOR_BUFFER_BIT);
    # /* 绘制一个白色多边形，指定四个顶点的坐标
    glColor3f (1.0, 1.0, 1.0);
    glBegin(GL_POLYGON);
    glVertex3f (0.25, 0.25, 0.0);
    glVertex3f (0.75, 0.25, 0.0);
    glVertex3f (0.75, 0.75, 0.0);
    glVertex3f (0.25, 0.75, 0.0);
    glEnd();
    # /* 不等待
    # * 立即开始处理保存在缓冲区中的 OpenGL 函数调用。
    # */
    glFlush ();

def init():
    # /* 制定清除颜色 */
    glClearColor (0.0, 0.0, 0.0, 0.0);
    # /* 设置投影变换方式 */
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0);

    
# /*
# *指定窗口的初始大小和位置以及显示模式（单缓存和 RGBA 模式）
# *打开一个标题为 hello 的窗口
# *调用 init 函数.
# *注册显示函数.
# * 进入主循环并处理事件.
# */

glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
glutInitWindowSize (250, 250);
glutInitWindowPosition (100, 100);
glutCreateWindow ("hello");
init ();
glutDisplayFunc(display);
glutMainLoop();