import image_process
import createModel
import capture

capture.capture()
image_process.imageProcess("photos/")
createModel.create_model("house")

#calling scripts and example usage
