function plotExitedAgents(data)
%plot time vs exited agents

fprintf("data.time: {%d} agents_exited {%d} ", data.time, data.agents_exited);

hold on;
plot(data.time, data.agents_exited, 'b.', 'MarkerSize', 10);
hold off;
