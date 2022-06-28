#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - prints Python strings.
 * @p: the PyUnicode Object to be printed
 *
 * Return: void, nth
 */
void print_python_string(PyObject *p)
{
	fflush(stdout);
	printf("[.] string object info\n");
	if PyUnicode_CheckExact(p)
	{
		printf("  type: ");
		if (PyUnicode_IS_COMPACT_ASCII(p))
			printf("compact ascii\n");
		else
			printf("compact unicode object\n");
		printf("  lenght: %zd\n", PyUnicode_GetLength(p));
		printf("  value: %ls\n", PyUnicode_AsWideCharString(p, NULL));
	}
	else
		printf("  [ERROR] Invalid String Object\n");
}
