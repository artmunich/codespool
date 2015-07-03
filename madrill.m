%Print a portrait of mandrill.

% Load the data for the mandrill image
load mandrill X map

% Create the image display using the image command
figure
image(X)

% Use the colormap specified in the image data file
colormap(map)

% Turn the axes off
axis off

% Add title
title('Mandrill')

% Pring image
print(gcf,'-dpng','mandrill')