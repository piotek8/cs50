


typedef struct sllist
{
    VALUE val;
    struct sllits* next;
}
sllnode;


//delete an entire linked list
void destroy (sllnode* head);


