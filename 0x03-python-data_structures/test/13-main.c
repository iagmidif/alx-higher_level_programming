#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    /* palindrome with even length */
    head = NULL;
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 17);
    if (is_palindrome(&head) == 1)
        printf("(Even) Linked list is a palindrome\n");
    else
        printf("(Even)Linked list is not a palindrome\n");

    free_listint(head);

    /* palindrome list with odd length */
    head = NULL;
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 17);
    if (is_palindrome(&head) == 1)
        printf("(ODD) Linked list is a palindrome\n");
    else
        printf("(ODD)Linked list is not a palindrome\n");

    free_listint(head);

    /* NOT palindome */
    head = NULL;
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 97);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 17);
    if (is_palindrome(&head) == 1)
        printf("Linked list is a palindrome\n");
    else
        printf("Linked list is not a palindrome\n");

    free_listint(head);
    /* An empty list is considered a palindrome */
    head = NULL;
    if (is_palindrome(&head) == 1)
	    printf("Empty list is a palindrome\n");
    else
	    printf("Empty list is not a palindrome\n");
	    
    return (0);
}
