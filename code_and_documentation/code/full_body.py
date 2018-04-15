import viz
import skeleton
import vizmenu
import vizinfo
import vizcam

viz.go()

		
def moveJoint(amount,slider,name):
	global model
	if name=='Head':
		bone=model.getBone('skel_Head')		
		euler=bone.getEuler(viz.ABS_PARENT)
		bone.lock()
		if slider=='Pan':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],amount,euler[2],viz.ABS_PARENT)
		elif slider=='Tilt':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],euler[1],amount,viz.ABS_PARENT)
		elif slider=='Lateral Flexion':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.ABS_PARENT)
	
	elif name=='Toracic Curve 1-4':
		bone=model.getBone('skel_Spine3')
		euler=bone.getEuler(viz.ABS_PARENT)
		bone.lock()		
		if slider=='Rotation':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],amount,euler[2],viz.ABS_PARENT)
		elif slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],euler[1],amount,viz.ABS_PARENT)
		elif slider=='Lateral Flexion':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.ABS_PARENT)
		
	elif name=='Toracic Curve 5-8':
		bone=model.getBone('skel_Spine2')
		euler=bone.getEuler(viz.ABS_PARENT)
		bone.lock()		
		if slider=='Rotation':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],amount,euler[2],viz.ABS_PARENT)
		elif slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],euler[1],amount,viz.ABS_PARENT)
		elif slider=='Lateral Flexion':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.ABS_PARENT)
			
	elif name=='Toracic Curve 9-12':
		bone=model.getBone('skel_Spine1')
		euler=bone.getEuler(viz.ABS_PARENT)
		bone.lock()		
		if slider=='Rotation':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],amount,euler[2],viz.ABS_PARENT)
		elif slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],euler[1],amount,viz.ABS_PARENT)
		elif slider=='Lateral Flexion':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.ABS_PARENT)

	elif name=='Lumbar Curve':
		bone=model.getBone('skel_Spine')
		euler=bone.getEuler(viz.ABS_PARENT)
		bone.lock()		
		if slider=='Rotation':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],amount,euler[2],viz.ABS_PARENT)
		elif slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],euler[1],amount,viz.ABS_PARENT)
		elif slider=='Lateral Flexion':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.ABS_PARENT)

	elif name=='Sternoclavicular Joint R':
		bone=model.getBone('skel_ShoulderR')
		euler=bone.getEuler(viz.AVATAR_LOCAL)
		bone.lock()		
		if slider=='Abduction/Adduction':
			amount=(amount-0.5)*(145)
			bone.setEuler(amount,euler[1],euler[2],viz.AVATAR_LOCAL)
		elif slider=='Elevation/Depression':
			amount=(amount-0.5)*(145)
			bone.setEuler(euler[0],euler[1],amount,viz.AVATAR_LOCAL)

	elif name=='Shoulder Joint R':
		bone=model.getBone('skel_ArmRU')
		euler=bone.getEuler(viz.AVATAR_LOCAL)
		bone.lock()		
		if slider=='Medial Rotation':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.AVATAR_LOCAL)
		elif slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],amount,euler[2],viz.AVATAR_LOCAL)
		elif slider=='Abduction/Adduction':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],euler[1],amount,viz.AVATAR_LOCAL)

	elif name=='Elbow Joint R':
		bone=model.getBone('skel_ArmRL')
		euler=bone.getEuler(viz.ABS_PARENT)
		bone.lock()		
		if slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],euler[1],amount,viz.ABS_PARENT)
		elif slider=='Pronotion/Supination':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],amount,euler[2],viz.ABS_PARENT)

	elif name=='Wrist Joint R':
		bone=model.getBone('skel_HandR')
		euler=bone.getEuler(viz.AVATAR_LOCAL)
		bone.lock()		
		if slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],euler[1],amount,viz.AVATAR_LOCAL)
		elif slider=='Abduction/Adduction':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.AVATAR_LOCAL)

	elif name=='Sternoclavicular Joint L':
		bone=model.getBone('skel_ShoulderL')
		euler=bone.getEuler(viz.AVATAR_LOCAL)
		bone.lock()		
		if slider=='Abduction/Adduction':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.AVATAR_LOCAL)
		elif slider=='Elevation/Depression':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],euler[1],amount,viz.AVATAR_LOCAL)

	elif name=='Shoulder Joint L':
		bone=model.getBone('skel_ArmLU')
		euler=bone.getEuler(viz.AVATAR_LOCAL)
		bone.lock()		
		if slider=='Medial Rotation':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.AVATAR_LOCAL)
		elif slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],amount,euler[2],viz.AVATAR_LOCAL)
		elif slider=='Abduction/Adduction':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],euler[1],amount,viz.AVATAR_LOCAL)

	elif name=='Elbow Joint L':
		bone=model.getBone('skel_ArmLL')
		euler=bone.getEuler(viz.ABS_PARENT)
		bone.lock()		
		if slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],euler[1],amount,viz.ABS_PARENT)
		elif slider=='Pronotion/Supination':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],amount,euler[2],viz.ABS_PARENT)

	elif name=='Wrist Joint L':
		bone=model.getBone('skel_HandL')
		euler=bone.getEuler(viz.AVATAR_LOCAL)
		bone.lock()		
		if slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],euler[1],amount,viz.AVATAR_LOCAL)
		elif slider=='Abduction/Adduction':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.AVATAR_LOCAL)
	
	elif name=='Hip Joint R':
		bone=model.getBone('skel_LegRU')
		euler=bone.getEuler(viz.AVATAR_LOCAL)
		bone.lock()		
		if slider=='Lateral/Medial Rot.':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.AVATAR_LOCAL)
		elif slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],amount,euler[2],viz.AVATAR_LOCAL)	
		elif slider=='Abduction/Adduction':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],euler[1],amount,viz.AVATAR_LOCAL)	
	
	elif name=='Knee Joint R':
		bone=model.getBone('skel_LegRL')
		euler=bone.getEuler(viz.AVATAR_LOCAL)
		bone.lock()		
		if slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],amount,euler[2],viz.AVATAR_LOCAL)	

	elif name=='Ankle Joint R':
		bone=model.getBone('skel_FootR')
		euler=bone.getEuler(viz.AVATAR_LOCAL)
		bone.lock()		
		if slider=='Dorsi/Plantar Flexion':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],amount,euler[2],viz.AVATAR_LOCAL)
		elif slider=='Inversion/Eversion':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],euler[1],amount,viz.AVATAR_LOCAL)

	elif name=='Hip Joint L':
		bone=model.getBone('skel_LegLU')
		euler=bone.getEuler(viz.AVATAR_LOCAL)
		bone.lock()		
		if slider=='Lateral/Medial Rot.':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.AVATAR_LOCAL)
		elif slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],amount,euler[2],viz.AVATAR_LOCAL)	
		elif slider=='Abduction/Adduction':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],euler[1],amount,viz.AVATAR_LOCAL)	
	
	elif name=='Knee Joint L':
		bone=model.getBone('skel_LegLL')
		euler=bone.getEuler(viz.AVATAR_LOCAL)
		bone.lock()		
		if slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],amount,euler[2],viz.AVATAR_LOCAL)	

	elif name=='Ankle Joint L':
		bone=model.getBone('skel_FootL')
		euler=bone.getEuler(viz.AVATAR_LOCAL)
		bone.lock()		
		if slider=='Dorsi/Plantar Flexion':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],amount,euler[2],viz.AVATAR_LOCAL)
		elif slider=='Inversion/Eversion':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],euler[1],amount,viz.AVATAR_LOCAL)


	
def setCurrentJoint(e):
	global panel
	if e.object.getItem(e.newSel)=='Head':
		panel.remove()
		panel=vizinfo.add('Head')
		slider1=panel.add(viz.SLIDER,'Pan')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Pan','Head')
		slider2=panel.add(viz.SLIDER,'Tilt')
		slider2.set(0.5)
		vizact.onslider(slider2,moveJoint,'Tilt','Head')
		slider3=panel.add(viz.SLIDER,'Lateral Flexion')
		slider3.set(0.5)
		vizact.onslider(slider3,moveJoint,'Lateral Flexion','Head')
	
	elif e.object.getItem(e.newSel)=='Toracic Curve 1-4':
		panel.remove()
		panel=vizinfo.add('Toracic Curve 1-4')
		slider1=panel.add(viz.SLIDER,'Flexion/Extension')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Flexion/Extension','Toracic Curve 1-4')
		slider2=panel.add(viz.SLIDER,'Lateral Flexion')
		slider2.set(0.5)
		vizact.onslider(slider2,moveJoint,'Lateral Flexion','Toracic Curve 1-4')
		slider3=panel.add(viz.SLIDER,'Rotation')
		slider3.set(0.5)
		vizact.onslider(slider3,moveJoint,'Rotation','Toracic Curve 1-4')

	elif e.object.getItem(e.newSel)=='Toracic Curve 5-8':
		panel.remove()
		panel=vizinfo.add('Toracic Curve 5-8')
		slider1=panel.add(viz.SLIDER,'Flexion/Extension')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Flexion/Extension','Toracic Curve 5-8')
		slider2=panel.add(viz.SLIDER,'Lateral Flexion')
		slider2.set(0.5)
		vizact.onslider(slider2,moveJoint,'Lateral Flexion','Toracic Curve 5-8')
		slider3=panel.add(viz.SLIDER,'Rotation')
		slider3.set(0.5)
		vizact.onslider(slider3,moveJoint,'Rotation','Toracic Curve 5-8')
		
	elif e.object.getItem(e.newSel)=='Toracic Curve 9-12':
		panel.remove()
		panel=vizinfo.add('Toracic Curve 9-12')
		slider1=panel.add(viz.SLIDER,'Flexion/Extension')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Flexion/Extension','Toracic Curve 9-12')
		slider2=panel.add(viz.SLIDER,'Lateral Flexion')
		slider2.set(0.5)
		vizact.onslider(slider2,moveJoint,'Lateral Flexion','Toracic Curve 9-12')
		slider3=panel.add(viz.SLIDER,'Rotation')
		slider3.set(0.5)
		vizact.onslider(slider3,moveJoint,'Rotation','Toracic Curve 9-12')

	elif e.object.getItem(e.newSel)=='Lumbar Curve':
		panel.remove()
		panel=vizinfo.add('Lumbar Curve')
		slider1=panel.add(viz.SLIDER,'Flexion/Extension')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Flexion/Extension','Lumbar Curve')
		slider2=panel.add(viz.SLIDER,'Lateral Flexion')
		slider2.set(0.5)
		vizact.onslider(slider2,moveJoint,'Lateral Flexion','Lumbar Curve')
		slider3=panel.add(viz.SLIDER,'Rotation')
		slider3.set(0.5)
		vizact.onslider(slider3,moveJoint,'Rotation','Lumbar Curve')
	
	elif e.object.getItem(e.newSel)=='Sternoclavicular Joint R':
		panel.remove()
		panel=vizinfo.add('Sternoclavicular Joint R')
		slider1=panel.add(viz.SLIDER,'Abduction/Adduction')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Abduction/Adduction','Sternoclavicular Joint R')
		slider2=panel.add(viz.SLIDER,'Elevation/Depression')
		slider2.set(0.5)
		vizact.onslider(slider2,moveJoint,'Elevation/Depression','Sternoclavicular Joint R')

	elif e.object.getItem(e.newSel)=='Shoulder Joint R':
		panel.remove()
		panel=vizinfo.add('Shoulder Joint R')
		slider1=panel.add(viz.SLIDER,'Medial Rotation')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Medial Rotation','Shoulder Joint R')
		slider2=panel.add(viz.SLIDER,'Flexion/Extension')
		slider2.set(0.5)
		vizact.onslider(slider2,moveJoint,'Flexion/Extension','Shoulder Joint R')
		slider3=panel.add(viz.SLIDER,'Abduction/Adduction')
		slider3.set(0.5)
		vizact.onslider(slider3,moveJoint,'Abduction/Adduction','Shoulder Joint R')		

	elif e.object.getItem(e.newSel)=='Elbow Joint R':
		panel.remove()
		panel=vizinfo.add('Elbow Joint R')
		slider1=panel.add(viz.SLIDER,'Flexion/Extension')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Flexion/Extension','Elbow Joint R')
		slider2=panel.add(viz.SLIDER,'Pronotion/Supination')
		slider2.set(0.5)
		vizact.onslider(slider2,moveJoint,'Pronotion/Supination','Elbow Joint R')
	
	elif e.object.getItem(e.newSel)=='Wrist Joint R':
		panel.remove()
		panel=vizinfo.add('Wrist Joint R')
		slider1=panel.add(viz.SLIDER,'Flexion/Extension')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Flexion/Extension','Wrist Joint R')
		slider2=panel.add(viz.SLIDER,'Abduction/Adduction')
		slider2.set(0.5)
		vizact.onslider(slider2,moveJoint,'Abduction/Adduction','Wrist Joint R')

	elif e.object.getItem(e.newSel)=='Sternoclavicular Joint L':
		panel.remove()
		panel=vizinfo.add('Sternoclavicular Joint L')
		slider1=panel.add(viz.SLIDER,'Abduction/Adduction')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Abduction/Adduction','Sternoclavicular Joint L')
		slider2=panel.add(viz.SLIDER,'Elevation/Depression')
		slider2.set(0.5)
		vizact.onslider(slider2,moveJoint,'Elevation/Depression','Sternoclavicular Joint L')

	elif e.object.getItem(e.newSel)=='Shoulder Joint L':
		panel.remove()
		panel=vizinfo.add('Shoulder Joint L')
		slider1=panel.add(viz.SLIDER,'Medial Rotation')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Medial Rotation','Shoulder Joint L')
		slider2=panel.add(viz.SLIDER,'Flexion/Extension')
		slider2.set(0.5)
		vizact.onslider(slider2,moveJoint,'Flexion/Extension','Shoulder Joint L')
		slider3=panel.add(viz.SLIDER,'Abduction/Adduction')
		slider3.set(0.5)
		vizact.onslider(slider3,moveJoint,'Abduction/Adduction','Shoulder Joint L')		

	elif e.object.getItem(e.newSel)=='Elbow Joint L':
		panel.remove()
		panel=vizinfo.add('Elbow Joint L')
		slider1=panel.add(viz.SLIDER,'Flexion/Extension')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Flexion/Extension','Elbow Joint L')
		slider2=panel.add(viz.SLIDER,'Pronotion/Supination')
		slider2.set(0.5)
		vizact.onslider(slider2,moveJoint,'Pronotion/Supination','Elbow Joint L')
	
	elif e.object.getItem(e.newSel)=='Wrist Joint L':
		panel.remove()
		panel=vizinfo.add('Wrist Joint L')
		slider1=panel.add(viz.SLIDER,'Flexion/Extension')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Flexion/Extension','Wrist Joint L')
		slider2=panel.add(viz.SLIDER,'Abduction/Adduction')
		slider2.set(0.5)
		vizact.onslider(slider2,moveJoint,'Abduction/Adduction','Wrist Joint L')

	elif e.object.getItem(e.newSel)=='Hip Joint R':
		panel.remove()
		panel=vizinfo.add('Hip Joint R')
		slider1=panel.add(viz.SLIDER,'Lateral/Medial Rot.')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Lateral/Medial Rot.','Hip Joint R')
		slider2=panel.add(viz.SLIDER,'Flexion/Extension')
		slider2.set(0.5)
		vizact.onslider(slider2,moveJoint,'Flexion/Extension','Hip Joint R')
		slider3=panel.add(viz.SLIDER,'Abduction/Adduction')
		slider3.set(0.5)
		vizact.onslider(slider3,moveJoint,'Abduction/Adduction','Hip Joint R')

	elif e.object.getItem(e.newSel)=='Knee Joint R':
		panel.remove()
		panel=vizinfo.add('Knee Joint R')
		slider1=panel.add(viz.SLIDER,'Flexion/Extension')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Flexion/Extension','Knee Joint R')
		
	elif e.object.getItem(e.newSel)=='Ankle Joint R':
		panel.remove()
		panel=vizinfo.add('Ankle Joint R')
		slider1=panel.add(viz.SLIDER,'Dorsi/Plantar Flexion')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Dorsi/Plantar Flexion','Ankle Joint R')
		slider2=panel.add(viz.SLIDER,'Inversion/Eversion')
		slider2.set(0.5)
		vizact.onslider(slider2,moveJoint,'Inversion/Eversion','Ankle Joint R')

	elif e.object.getItem(e.newSel)=='Hip Joint L':
		panel.remove()
		panel=vizinfo.add('Hip Joint L')
		slider1=panel.add(viz.SLIDER,'Lateral/Medial Rot.')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Lateral/Medial Rot.','Hip Joint L')
		slider2=panel.add(viz.SLIDER,'Flexion/Extension')
		slider2.set(0.5)
		vizact.onslider(slider2,moveJoint,'Flexion/Extension','Hip Joint L')
		slider3=panel.add(viz.SLIDER,'Abduction/Adduction')
		slider3.set(0.5)
		vizact.onslider(slider3,moveJoint,'Abduction/Adduction','Hip Joint L')

	elif e.object.getItem(e.newSel)=='Knee Joint L':
		panel.remove()
		panel=vizinfo.add('Knee Joint L')
		slider1=panel.add(viz.SLIDER,'Flexion/Extension')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Flexion/Extension','Knee Joint L')
		
	elif e.object.getItem(e.newSel)=='Ankle Joint L':
		panel.remove()
		panel=vizinfo.add('Ankle Joint L')
		slider1=panel.add(viz.SLIDER,'Dorsi/Plantar Flexion')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Dorsi/Plantar Flexion','Ankle Joint L')
		slider2=panel.add(viz.SLIDER,'Inversion/Eversion')
		slider2.set(0.5)
		vizact.onslider(slider2,moveJoint,'Inversion/Eversion','Ankle Joint L')

	return panel
			
			
model=viz.add('male.cfg',alpha=0.5)
model.setEuler(180,0,0)

vizact.onkeydown(' ',model.visible,viz.TOGGLE)

cam = vizcam.PivotNavigate(distance=3)
cam.centerNode(model)

skeleton.createSkeletonFullBody()



panel=vizinfo.add('Head')
slider1=panel.add(viz.SLIDER,'Pan')
slider1.set(0.5)
vizact.onslider(slider1,moveJoint,'Pan','Head')
slider2=panel.add(viz.SLIDER,'Tilt')
slider2.set(0.5)
vizact.onslider(slider2,moveJoint,'Tilt','Head')
slider3=panel.add(viz.SLIDER,'Lateral Flexion')
slider3.set(0.5)
vizact.onslider(slider3,moveJoint,'Lateral Flexion','Head')


menu=vizmenu.add()
menu.setAutoHide(viz.OFF)
joint_menu=menu.add('Pick a Joint >>>')

sub_menu1=joint_menu.add(vizmenu.MENU,'Torso-Head Branch')
list1=sub_menu1.add(viz.DROPLIST)
list1.addItems(['Head'])
list1.addItems(['Toracic Curve 1-4'])
list1.addItems(['Toracic Curve 5-8'])
list1.addItems(['Toracic Curve 9-12'])
list1.addItems(['Lumbar Curve'])
vizact.onlist(list1,setCurrentJoint)

sub_menu2=joint_menu.add(vizmenu.MENU,'Torso-Right Hand Branch')
list2=sub_menu2.add(viz.DROPLIST)
list2.addItems(['Sternoclavicular Joint R'])
list2.addItems(['Shoulder Joint R'])
list2.addItems(['Elbow Joint R'])
list2.addItems(['Wrist Joint R'])
vizact.onlist(list2,setCurrentJoint)

sub_menu3=joint_menu.add(vizmenu.MENU,'Torso-Left Hand Branch')
list3=sub_menu3.add(viz.DROPLIST)
list3.addItems(['Sternoclavicular Joint L'])
list3.addItems(['Shoulder Joint L'])
list3.addItems(['Elbow Joint L'])
list3.addItems(['Wrist Joint L'])
vizact.onlist(list3,setCurrentJoint)

sub_menu4=joint_menu.add(vizmenu.MENU,'Torso-Right Foot Branch')
list4=sub_menu4.add(viz.DROPLIST)
list4.addItems(['Hip Joint R'])
list4.addItems(['Knee Joint R'])
list4.addItems(['Ankle Joint R'])
vizact.onlist(list4,setCurrentJoint)

sub_menu5=joint_menu.add(vizmenu.MENU,'Torso-Left Foot Branch')
list5=sub_menu5.add(viz.DROPLIST)
list5.addItems(['Hip Joint L'])
list5.addItems(['Knee Joint L'])
list5.addItems(['Ankle Joint L'])
vizact.onlist(list5,setCurrentJoint)

	
		


