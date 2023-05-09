#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - ...
 * @head: ...
 * @number: ...
 * Return: ...
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *tmp = *head;

        new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;
	if (tmp == NULL || tmp->n >= number)
	{
		new_node->next = tmp;
		*head = new_node;
		return (new_node);
	}
	while(tmp && tmp->next && tmp->n < number)
	{
		tmp->next = tmp;
	}
	new_node = tmp->next;
	tmp->next = new_node;
	return (new_node);
}
