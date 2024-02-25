# -*- coding = utf-8 -*-
# @Time : 10/21/2023 2:20 AM
# @Author : Lauren
# @File : TruckPosition.py
# @Software : PyCharm

from dataclasses import dataclass, replace


@dataclass
class TruckPosition:
    x: float
    y: float


@dataclass
class TruckPositionDelta:
    truck_id: int
    delta_x: float
    delta_y: float


class Subscriber:
    def __init__(self, server):
        pass

    def process_update(self, update):
        pass

    def subscribe_to_truck(self, truck_id, client_id):
        return TruckPosition(0, 0)

    def get_updates(self, client_id):
        return [TruckPositionDelta(0, 0, 0)]


class Server:
    def __init__(self):
        self.registered_trucks = set()
        self.current_pos = {}

    def subscribe_to_truck(self, truck_id):
        self.registered_trucks.add(truck_id)
        # return replace(self.current_pos([truck_id])

    def add_position(self, truck_id, pos):
        self.current_pos[truck_id] = pos


class Subscriber {
private:
    unordered_map < int, vector < int >> subscribers;
    unordered_map < int, vector < TruckPositionDelta < double >> > updates;
    public:
    Server


server;
Subscriber(Server
server){
    this->server = server;
}
void
process_update(const
TruckPositionDelta < double > & update) {
                                        // Implement
the
processing
of
the
update
here
double
curr_x = server.truck_pos[update.truck_id].x;
double
curr_y = server.truck_pos[update.truck_id].y;
curr_x += update.delta_x;
curr_y += update.delta_y;
server.add_position(update.truck_id, {curr_x, curr_y});
for (auto i:subscribers[update.truck_id])
{
    updates[i].push_back(update);
}

}

TruckPosition < double > subscribe_to_truck(int
truck_id, int
client_id) {
           // Return
the
default
TruckPosition
for demonstration purposes
subscribers[truck_id].push_back(client_id);
return server.subscribe_to_truck(truck_id);
}

std::vector < TruckPositionDelta < double >> get_updates(int
client_id) {
// Return
the
default
TruckPositionDelta
for demonstration purposes
    vector < TruckPositionDelta < double >> v = updates[client_id];
updates[client_id].clear();
return v;
}
};

// Define
Server


class
    class Server {

    public:
        unordered_map < int, TruckPosition < double >> truck_pos;
        Server()

    {

    }

    TruckPosition < double > subscribe_to_truck(int
    truck_id) {


return truck_pos[truck_id];
}

void
add_position(int
truck_id, const
TruckPosition < double > & pos) {
truck_pos[truck_id] = pos;
}

};
