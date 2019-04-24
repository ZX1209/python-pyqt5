# not finished

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


year = 0
day = 0
def init():
    glClearColor (0.0, 0.0, 0.0, 0.0);
    glShadeModel (GL_FLAT);

def display():
    glClear (GL_COLOR_BUFFER_BIT);
    glColor3f (1.0, 1.0, 1.0);
    glPushMatrix();
    glutWireSphere((1.0, 20, 16)); /* 绘制太阳 */
    glRotatef ((GLfloat) year, 0.0, 1.0, 0.0);
    glTranslatef (2.0, 0.0, 0.0);
    glRotatef ((GLfloat) day, 0.0, 1.0, 0.0);
    glutWireSphere(0.2, 10, 8); /* 绘制行星 */
    glPopMatrix();
    glutSwapBuffers();


def reshape (w, h)
    glViewport (0, 0, (GLsizei) w, (GLsizei) h);
    glMatrixMode (GL_PROJECTION);
    glLoadIdentity ();
    gluPerspective(60.0, (GLfloat) w/(GLfloat) h, 1.0, 20.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt (0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);

def keyboard (key, x, y):
    switch (key) {
        case 'd':
        day = (day + 10) % 360;
        glutPostRedisplay();
        break;
        case 'D':
        day = (day - 10) % 360;
        glutPostRedisplay();
        break;
        case 'y':
        year = (year + 5) % 360;
        glutPostRedisplay();
        break;
        case 'Y':
        year = (year - 5) % 360;
        glutPostRedisplay();
        break;
        case 27:
        exit(0);
        break;
        default:
        break;
        }
    }


def main()
    glutInit(sys.argv);
    glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize (500, 500);
    glutInitWindowPosition (100, 100);
    glutCreateWindow (argv[0]);
    init ();
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutKeyboardFunc(keyboard);
    glutMainLoop();

if __name__ == "__main__":
    main()