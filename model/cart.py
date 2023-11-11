
class Cart:

    def __init__(self):
        self.clothes = []
        self.onAddCallbacks = []
        self.onRemoveCallbacks = []
        self.onUpdateCallbacks = []

    def add_clothes(self, clothes_id, clothes_count=1):
        self.clothes.append([clothes_id, clothes_count])
        self.callOnAddEvent(clothes_id, clothes_count)

    def remove_clothes(self, clothes_id):
        for i in range(len(self.clothes)):
            if self.clothes[i][0] == clothes_id:
                self.clothes.pop(i)
                break

        self.callOnRemoveEvent(clothes_id)

    def update_clothes(self, clothes_id, clothes_count=1):
        for index, clothes in enumerate(self.clothes):
            if clothes[0] == clothes_id:
                self.clothes[index] = [clothes_id, clothes_count]
                break

        self.callOnUpdateEvent(clothes_id, clothes_count)

    def get_clothes(self):
        return self.clothes

    def get_clothes_ids(self):
        return [clothes[0] for clothes in self.clothes]

    def addOnAddCallback(self, callback):
        self.onAddCallbacks.append(callback)

    def addOnRemoveCallback(self, callback):
        self.onRemoveCallbacks.append(callback)

    def addOnUpdateCallback(self, callback):
        self.onUpdateCallbacks.append(callback)

    def clear_cart(self):
        self.clothes.clear()

        for callback in self.onRemoveCallbacks:
            callback(-1)

    def callOnAddEvent(self, clothes_id, clothes_count=1):
        for callback in self.onAddCallbacks:
            callback(clothes_id, clothes_count)

    def callOnRemoveEvent(self, clothes_id):
        for callback in self.onRemoveCallbacks:
            callback(clothes_id)

    def callOnUpdateEvent(self, clothes_id,clothes_count=1):
        for callback in self.onUpdateCallbacks:
            callback(clothes_id, clothes_count)
