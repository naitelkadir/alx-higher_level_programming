#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_list(PyObject* p) {
    if (!PyList_Check(p)) {
        printf("Invalid Python list object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the list = %zd\n", size);

    printf("[*] Allocated = %zd\n", ((PyListObject*)p)->allocated);
    for (Py_ssize_t i = 0; i < size; ++i) {
        PyObject* item = PyList_GetItem(p, i);
        const char* type = Py_TYPE(item)->tp_name;
        printf("Element %zd: %s\n", i, type);
    }
}

void print_python_bytes(PyObject* p) {
    if (!PyBytes_Check(p)) {
        printf("Invalid Python bytes object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    printf("[.] Bytes object info\n");
    printf("  - Length: %zd\n", size);

    const char* data = PyBytes_AsString(p);
    printf("  - Content: ");

    if (size > 10)
        size = 10;

    for (Py_ssize_t i = 0; i < size; ++i) {
        printf("%02hhx", data[i]);
        if (i < size - 1)
            printf(" ");
    }

    printf("\n");
}
