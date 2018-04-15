import viz
import skeleton
import vizmenu
import vizinfo
import vizcam
viz.go()


def moveJoint(amount,slider,name):
	global model
	if name=='Wrist':
		bone=model.getBone('bone WRIST')		
		euler=bone.getEuler(viz.ABS_PARENT)
		bone.lock()
		if slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.ABS_PARENT)
		elif slider=='Abduction/Adduction':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],euler[1],amount,viz.ABS_PARENT)
		
	elif name=='Carpometacarpal Joint T':
		bone=model.getBone('bone thumb ROOT')		
		euler=bone.getEuler(viz.ABS_PARENT)
		bone.lock()
		if slider=='Lateral/Medial Rotation':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.ABS_PARENT)
		elif slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],euler[1],amount,viz.ABS_PARENT)

	elif name=='Metacarpophalangeal Joint T':
		bone=model.getBone('bone thumb 0-0')		
		euler=bone.getEuler(viz.ABS_PARENT)
		bone.lock()
		if slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],euler[1],amount,viz.ABS_PARENT)

	elif name=='Interphalangeal Joint T':
		bone=model.getBone('bone thumb 0-1')		
		euler=bone.getEuler(viz.ABS_PARENT)
		bone.lock()
		if slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],euler[1],amount,viz.ABS_PARENT)
			
	elif name=='Metacarpophalangeal Joint L':
		bone=model.getBone('bone little 4-0')		
		euler=bone.getEuler(viz.ABS_PARENT)
		bone.lock()
		if slider=='Aduction/Abbduction':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.ABS_PARENT)
		elif slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.ABS_PARENT)
	
	elif name=='Proximal Interphalangeal Joint L':
		bone=model.getBone('bone little 4-1')		
		euler=bone.getEuler(viz.ABS_PARENT)
		bone.lock()
		if slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.ABS_PARENT)

	elif name=='Distal Interphalangeal Joint L':
		bone=model.getBone('bone little 4-2')		
		euler=bone.getEuler(viz.ABS_PARENT)
		bone.lock()
		if slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.ABS_PARENT)

	elif name=='Metacarpophalangeal Joint R':
		bone=model.getBone('bone ring 3-0')		
		euler=bone.getEuler(viz.ABS_PARENT)
		bone.lock()
		if slider=='Aduction/Abbduction':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],euler[1],amount,viz.ABS_PARENT)
		elif slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.ABS_PARENT)
	
	elif name=='Proximal Interphalangeal Joint R':
		bone=model.getBone('bone ring 3-1')		
		euler=bone.getEuler(viz.ABS_PARENT)
		bone.lock()
		if slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.ABS_PARENT)

	elif name=='Distal Interphalangeal Joint R':
		bone=model.getBone('bone ring 3-2')		
		euler=bone.getEuler(viz.ABS_PARENT)
		bone.lock()
		if slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.ABS_PARENT)

	elif name=='Metacarpophalangeal Joint M':
		bone=model.getBone('bone middle 2-0')		
		euler=bone.getEuler(viz.ABS_PARENT)
		bone.lock()
		if slider=='Aduction/Abbduction':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],euler[1],amount,viz.ABS_PARENT)
		elif slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.ABS_PARENT)
	
	elif name=='Proximal Interphalangeal Joint M':
		bone=model.getBone('bone middle 2-1')		
		euler=bone.getEuler(viz.ABS_PARENT)
		bone.lock()
		if slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.ABS_PARENT)

	elif name=='Distal Interphalangeal Joint M':
		bone=model.getBone('bone middle 2-2')		
		euler=bone.getEuler(viz.ABS_PARENT)
		bone.lock()
		if slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.ABS_PARENT)

	elif name=='Metacarpophalangeal Joint I':
		bone=model.getBone('bone index 1-0')		
		euler=bone.getEuler(viz.ABS_PARENT)
		bone.lock()
		if slider=='Aduction/Abbduction':
			amount=(amount-0.5)*145
			bone.setEuler(euler[0],euler[1],amount,viz.ABS_PARENT)
		elif slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.ABS_PARENT)
	
	elif name=='Proximal Interphalangeal Joint I':
		bone=model.getBone('bone index 1-1')		
		euler=bone.getEuler(viz.ABS_PARENT)
		bone.lock()
		if slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.ABS_PARENT)

	elif name=='Distal Interphalangeal Joint I':
		bone=model.getBone('bone index 1-2')		
		euler=bone.getEuler(viz.ABS_PARENT)
		bone.lock()
		if slider=='Flexion/Extension':
			amount=(amount-0.5)*145
			bone.setEuler(amount,euler[1],euler[2],viz.ABS_PARENT)




def setCurrentJoint(e):
	global panel
	if e.object.getItem(e.newSel)=='Wrist Joint':
		panel.remove()
		panel=vizinfo.add('Wrist Joint')
		slider1=panel.add(viz.SLIDER,'Flexion/Extension')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Flexion/Extension','Wrist')
		slider2=panel.add(viz.SLIDER,'Abduction/Adduction')
		slider2.set(0.5)
		vizact.onslider(slider2,moveJoint,'Abduction/Adduction','Wrist')
	
	elif e.object.getItem(e.newSel)=='Carpometacarpal Joint T':
		panel.remove()
		panel=vizinfo.add('Carpometacarpal Joint T')
		slider1=panel.add(viz.SLIDER,'Lateral/Medial Rotation')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Lateral/Medial Rotation','Carpometacarpal Joint T')
		slider2=panel.add(viz.SLIDER,'Flexion/Extension')
		slider2.set(0.5)
		vizact.onslider(slider2,moveJoint,'Flexion/Extension','Carpometacarpal Joint T')
		
	elif e.object.getItem(e.newSel)=='Metacarpophalangeal Joint T':
		panel.remove()
		panel=vizinfo.add('Carpometacarpal Joint T')
		slider1=panel.add(viz.SLIDER,'Flexion/Extension')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Flexion/Extension','Metacarpophalangeal Joint T')
	
	elif e.object.getItem(e.newSel)=='Interphalangeal Joint T':
		panel.remove()
		panel=vizinfo.add('Interphalangeal Joint T')
		slider1=panel.add(viz.SLIDER,'Flexion/Extension')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Flexion/Extension','Interphalangeal Joint T')	
	
	elif e.object.getItem(e.newSel)=='Metacarpophalangeal Joint L':
		panel.remove()
		panel=vizinfo.add('Metacarpophalangeal Joint L')
		slider1=panel.add(viz.SLIDER,'Aduction/Abbduction')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Aduction/Abbduction','Metacarpophalangeal Joint L')
		slider2=panel.add(viz.SLIDER,'Flexion/Extension')
		slider2.set(0.5)
		vizact.onslider(slider2,moveJoint,'Flexion/Extension','Metacarpophalangeal Joint L')
		
	elif e.object.getItem(e.newSel)=='Proximal Interphalangeal Joint L':
		panel.remove()
		panel=vizinfo.add('Proximal Interphalangeal Joint L')
		slider1=panel.add(viz.SLIDER,'Flexion/Extension')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Flexion/Extension','Proximal Interphalangeal Joint L')
		
	elif e.object.getItem(e.newSel)=='Distal Interphalangeal Joint L':
		panel.remove()
		panel=vizinfo.add('Distal Interphalangeal Joint L')
		slider1=panel.add(viz.SLIDER,'Flexion/Extension')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Flexion/Extension','Distal Interphalangeal Joint L')		

	elif e.object.getItem(e.newSel)=='Metacarpophalangeal Joint R':
		panel.remove()
		panel=vizinfo.add('Metacarpophalangeal Joint R')
		slider1=panel.add(viz.SLIDER,'Aduction/Abbduction')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Aduction/Abbduction','Metacarpophalangeal Joint R')
		slider2=panel.add(viz.SLIDER,'Flexion/Extension')
		slider2.set(0.5)
		vizact.onslider(slider2,moveJoint,'Flexion/Extension','Metacarpophalangeal Joint R')
		
	elif e.object.getItem(e.newSel)=='Proximal Interphalangeal Joint R':
		panel.remove()
		panel=vizinfo.add('Proximal Interphalangeal Joint R')
		slider1=panel.add(viz.SLIDER,'Flexion/Extension')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Flexion/Extension','Proximal Interphalangeal Joint R')
		
	elif e.object.getItem(e.newSel)=='Distal Interphalangeal Joint R':
		panel.remove()
		panel=vizinfo.add('Distal Interphalangeal Joint R')
		slider1=panel.add(viz.SLIDER,'Flexion/Extension')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Flexion/Extension','Distal Interphalangeal Joint R')		

	elif e.object.getItem(e.newSel)=='Metacarpophalangeal Joint M':
		panel.remove()
		panel=vizinfo.add('Metacarpophalangeal Joint M')
		slider1=panel.add(viz.SLIDER,'Aduction/Abbduction')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Aduction/Abbduction','Metacarpophalangeal Joint M')
		slider2=panel.add(viz.SLIDER,'Flexion/Extension')
		slider2.set(0.5)
		vizact.onslider(slider2,moveJoint,'Flexion/Extension','Metacarpophalangeal Joint M')
		
	elif e.object.getItem(e.newSel)=='Proximal Interphalangeal Joint M':
		panel.remove()
		panel=vizinfo.add('Proximal Interphalangeal Joint M')
		slider1=panel.add(viz.SLIDER,'Flexion/Extension')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Flexion/Extension','Proximal Interphalangeal Joint M')
		
	elif e.object.getItem(e.newSel)=='Distal Interphalangeal Joint M':
		panel.remove()
		panel=vizinfo.add('Distal Interphalangeal Joint M')
		slider1=panel.add(viz.SLIDER,'Flexion/Extension')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Flexion/Extension','Distal Interphalangeal Joint M')	

	elif e.object.getItem(e.newSel)=='Metacarpophalangeal Joint I':
		panel.remove()
		panel=vizinfo.add('Metacarpophalangeal Joint I')
		slider1=panel.add(viz.SLIDER,'Aduction/Abbduction')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Aduction/Abbduction','Metacarpophalangeal Joint I')
		slider2=panel.add(viz.SLIDER,'Flexion/Extension')
		slider2.set(0.5)
		vizact.onslider(slider2,moveJoint,'Flexion/Extension','Metacarpophalangeal Joint I')
		
	elif e.object.getItem(e.newSel)=='Proximal Interphalangeal Joint I':
		panel.remove()
		panel=vizinfo.add('Proximal Interphalangeal Joint I')
		slider1=panel.add(viz.SLIDER,'Flexion/Extension')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Flexion/Extension','Proximal Interphalangeal Joint I')
		
	elif e.object.getItem(e.newSel)=='Distal Interphalangeal Joint I':
		panel.remove()
		panel=vizinfo.add('Distal Interphalangeal Joint I')
		slider1=panel.add(viz.SLIDER,'Flexion/Extension')
		slider1.set(0.5)
		vizact.onslider(slider1,moveJoint,'Flexion/Extension','Distal Interphalangeal Joint I')	



	return panel





model=viz.add('hand.cfg',alpha=0.5)

vizact.onkeydown(' ',model.visible,viz.TOGGLE)
import vizcam
cam = vizcam.PivotNavigate(distance=0.5)
cam.centerNode(model)

skeleton.createSkeletonHand()


panel=vizinfo.add('Wrist Joint')
slider1=panel.add(viz.SLIDER,'Flexion/Extension')
slider1.set(0.5)
vizact.onslider(slider1,moveJoint,'Flexion/Extension','Wrist')
slider2=panel.add(viz.SLIDER,'Abduction/Adduction')
slider2.set(0.5)
vizact.onslider(slider2,moveJoint,'Abduction/Adduction','Wrist')

menu=vizmenu.add()
menu.setAutoHide(viz.OFF)
joint_menu=menu.add('Pick a Joint >>>')

sub_menu1=joint_menu.add(vizmenu.MENU,'Wrist')
list1=sub_menu1.add(viz.DROPLIST)
list1.addItems(['Wrist Joint'])
vizact.onlist(list1,setCurrentJoint)

sub_menu2=joint_menu.add(vizmenu.MENU,'Thumb Finger')
list2=sub_menu2.add(viz.DROPLIST)
list2.addItems(['Carpometacarpal Joint T'])
list2.addItems(['Metacarpophalangeal Joint T'])
list2.addItems(['Interphalangeal Joint T'])
vizact.onlist(list2,setCurrentJoint)

sub_menu3=joint_menu.add(vizmenu.MENU,'Little Finger')
list3=sub_menu3.add(viz.DROPLIST)
list3.addItems(['Metacarpophalangeal Joint L'])
list3.addItems(['Proximal Interphalangeal Joint L'])
list3.addItems(['Distal Interphalangeal Joint L'])
vizact.onlist(list3,setCurrentJoint)

sub_menu4=joint_menu.add(vizmenu.MENU,'Ring Finger')
list4=sub_menu4.add(viz.DROPLIST)
list4.addItems(['Metacarpophalangeal Joint R'])
list4.addItems(['Proximal Interphalangeal Joint R'])
list4.addItems(['Distal Interphalangeal Joint R'])
vizact.onlist(list4,setCurrentJoint)

sub_menu5=joint_menu.add(vizmenu.MENU,'Middle Finger')
list5=sub_menu5.add(viz.DROPLIST)
list5.addItems(['Metacarpophalangeal Joint M'])
list5.addItems(['Proximal Interphalangeal Joint M'])
list5.addItems(['Distal Interphalangeal Joint M'])
vizact.onlist(list5,setCurrentJoint)

sub_menu6=joint_menu.add(vizmenu.MENU,'Index Finger')
list6=sub_menu6.add(viz.DROPLIST)
list6.addItems(['Metacarpophalangeal Joint I'])
list6.addItems(['Proximal Interphalangeal Joint I'])
list6.addItems(['Distal Interphalangeal Joint I'])
vizact.onlist(list6,setCurrentJoint)