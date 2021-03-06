resource "aws_instance" "jumpbox" {
  availability_zone = local.availability_zones[0]

  ami = data.aws_ami.base_linux.id
  instance_type = "t2.micro"
  key_name = "kainos-dev"
  iam_instance_profile = "TerraformJumpboxRole"
  vpc_security_group_ids = [aws_security_group.jumpbox_sg.id]
  subnet_id = aws_subnet.public_subnet.id
  user_data = data.template_cloudinit_config.jumpbox_user_data.rendered
  associate_public_ip_address = true

  tags = merge(local.default_tags, {
     Name = "${local.resource_prefix}-jumpbox"
  })
}
