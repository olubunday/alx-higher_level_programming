#include <Python.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <listobject.h>
#include <math.h>
#include <object.h>

/**
 * print_python_bytes - print information about Python bytes objects
 * @p: pointer to a PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, limit;
	PyBytesObject *b;
	PyVarObject *o;

	b = (PyBytesObject *)p;
	o = (PyVarObject *)p;
	puts("[.] bytes object info");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		puts("  [ERROR] Invalid Bytes Object");
		fflush(stdout);
		return;
	}
	printf("  size: %ld\n", o->ob_size);
	printf("  trying string: ");
	for (i = 0; i < o->ob_size && b->ob_sval[i] != '\0'; i++)
		putchar(b->ob_sval[i] > 0 ? b->ob_sval[i] : '?');
	putchar('\n');
	limit = o->ob_size + 1 > 10 ? 10 : o->ob_size + 1;
	printf("  first %ld bytes: ", limit);
	for (i = 0; i < limit; i++)
	{
		printf("%02hx", (unsigned char)b->ob_sval[i]);
		if (i < limit - 1)
			putchar(' ');
	}
	putchar('\n');
	fflush(stdout);
}


/**
 * print_python_float - print information about Python float objects
 * @p: pointer to a PyFloatObject (cast as a PyObject)
 */
void print_python_float(PyObject *p)
{
	char *repr;
	PyFloatObject *f;

	f = (PyFloatObject *)p;
	puts("[.] float object info");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		puts("  [ERROR] Invalid Float Object");
		fflush(stdout);
		return;
	}
	repr = PyOS_double_to_string(f->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", repr);
	PyMem_Free(repr);
	fflush(stdout);
}


/**
 * print_python_list - print information about Python list objects
 * @p: pointer to a PyListObject (cast as a PyObject)
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i;
	PyListObject *l;
	PyVarObject *o;

	l = (PyListObject *)p;
	o = (PyVarObject *)p;
	puts("[*] Python list info");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		puts("  [ERROR] Invalid List Object");
		fflush(stdout);
		return;
	}
	printf("[*] Size of the Python List = %ld\n", o->ob_size);
	printf("[*] Allocated = %ld\n", l->allocated);
	for (i = 0; i < o->ob_size; i++)
	{
		printf("Element %ld: %s\n", i, l->ob_item[i]->ob_type->tp_name);
		if (strcmp(l->ob_item[i]->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(l->ob_item[i]);
		else if (strcmp(l->ob_item[i]->ob_type->tp_name, "float") == 0)
			print_python_float(l->ob_item[i]);
	}
	fflush(stdout);
}


/**
 * print_python_string - print information about Python str objects
 * @p: pointer to a PyASCIIObject or a PyCompactUnicodeObject
 */
void print_python_string(PyObject *p)
{
	PyASCIIObject *a;

	a = (PyASCIIObject *)p;
	puts("[.] string object info");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		puts("  [ERROR] Invalid String Object");
		fflush(stdout);
		return;
	}
	if (a->state.compact && a->state.ascii)
	{
		puts("  type: compact ascii");
		printf("  length: %ld\n", a->length);
		printf("  value: %s\n", (char *)(a + 1));
	}
	else if (a->state.compact && !a->state.ascii)
	{
		puts("  type: compact unicode object");
		printf("  length: %ld\n", a->length);
		printf("  value: %s\n", PyUnicode_AsUTF8(p));
	}
	fflush(stdout);
}
