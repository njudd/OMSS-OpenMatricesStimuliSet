def save(self,  # so self is the object we assigned (i.e., rpm)
         path,  # argq
         puzzle_name,  # arg2
         background_color=255,  # arg4 with defaults... etc

         ##############
         image_size=750, # CHANGE THE Default to 750
         ##############

         line_thickness=3,
         shape_border_thickness=2):
    image_size, background_color, line_thickness, shape_border_thickness = \
        int(abs(image_size)), int(abs(background_color)), int(abs(line_thickness)), int(abs(shape_border_thickness))
    assert (image_size != 0 and background_color <= 255)
    img = self.generate_matrix(self.answer, background_color, image_size,
                               line_thickness, shape_border_thickness)

    # Ann will have some stuff here to colorize

    corner_rightbottom = ((image_size/3)*2 +5) # assuming a 3by3 grid, adding 5 to get rid of lines
    ans_3x3 = img[corner_rightbottom:, corner_rightbottom:] # this gets you to the bottom right stimuli on a 3x3 grid

    # goals to make a stim that has the lower corner as white

    # you subset the lower right corner of the stimuli object and than fill with white
    M = (image_size/3) -5)*2 # I think times 2 because of the dimensions
    whole_img[whole_img == [corner_rightbottom:, corner_rightbottom:]] = [0, 0, 0] * M # where M is the dimension of subseted space (ideally take image size to define)

    # than subset the answer and save both (copy line ***)


    self.ans_ImageNum = img  # here I save the img to the object (self) in this function

    img = Image.fromarray(img)  # making it an image since I took it away form the return of generate_matrix
    # np.savetxt(os.path.join(path, puzzle_name + "_answerY.png"), img)
    img.save(os.path.join(path, puzzle_name + "_answer.png"))


    for i, alternative in enumerate(self.alternatives):
        img = self.generate_matrix(alternative, background_color,
                                   image_size, line_thickness,
                                   shape_border_thickness)


        img = Image.fromarray(img)  # making it an image

        # just subset after Ann's stuff
        img.save(os.path.join(path, puzzle_name + f"_alternative_{i}.png"))
