class Node {
    public:
        int k; int v; Node* prev; Node* next;
        Node(int k, int v): k(k), v(v), prev(nullptr), next(nullptr){}
};

class LRUCache {
    private:
       Node* start;
       Node* end;
       unordered_map<int,Node*> mp;
       int cap;

    void ins(Node* n) {
        Node* temp = end->prev;
        temp->next = n;
        n->prev = temp;
        n->next = end;
        end->prev = n;
    }

    void dele(int k) {
        Node* n = mp[k];
        Node* temp = n->prev;
        temp->next = n->next;
        n->next->prev = temp;
    }

public:
    LRUCache(int capacity) {
        cap = capacity;
        mp.clear();
        start = new Node(0,0);
        end = new Node(0,0);
        start->next = end;
        end->prev = start;
    }
    
    int get(int key) {
        if (mp.count(key)!=1)
            return -1;
        dele(key);
        ins(mp[key]);
        return mp[key]->v;
    }
    
    void put(int key, int value) {
        if (mp.count(key)==1) {
            Node* n = mp[key];
            dele(key);
            n->v = value;
            ins(n);
            mp[key] = n;
        } else {
            Node* n = new Node(key, value);
            ins(n);
            mp[key] = n;
            if (size(mp) > cap) {
                Node* lru = start->next;
                dele(lru->k);
                mp.erase(lru->k);
                delete lru;
            }
        }

    }
};
